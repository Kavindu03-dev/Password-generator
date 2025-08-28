import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import random
import string
import pyperclip
import json
import os
from datetime import datetime

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator Pro")
        self.window.geometry("600x700")
        self.window.configure(bg='#2c3e50')
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', padding=10, font=('Arial', 10))
        style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 10))
        style.configure('TCheckbutton', background='#2c3e50', foreground='white')
        
        self.setup_ui()
        self.load_saved_passwords()
        
    def setup_ui(self):
        # Main title
        title_label = tk.Label(
            self.window, 
            text="🔐 Password Generator Pro", 
            font=('Arial', 20, 'bold'),
            bg='#2c3e50',
            fg='#ecf0f1'
        )
        title_label.pack(pady=20)
        
        # Password length frame
        length_frame = tk.Frame(self.window, bg='#2c3e50')
        length_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(length_frame, text="Password Length:", bg='#2c3e50', fg='white', font=('Arial', 12)).pack(side='left')
        
        self.length_var = tk.StringVar(value="16")
        length_spinbox = tk.Spinbox(
            length_frame, 
            from_=4, 
            to=128, 
            textvariable=self.length_var,
            width=10,
            font=('Arial', 12)
        )
        length_spinbox.pack(side='right')
        
        # Character options frame
        options_frame = tk.LabelFrame(
            self.window, 
            text="Character Options", 
            bg='#2c3e50', 
            fg='white',
            font=('Arial', 12, 'bold')
        )
        options_frame.pack(pady=10, padx=20, fill='x')
        
        # Checkboxes
        self.uppercase_var = tk.BooleanVar(value=True)
        self.lowercase_var = tk.BooleanVar(value=True)
        self.numbers_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.similar_var = tk.BooleanVar(value=False)
        self.ambiguous_var = tk.BooleanVar(value=False)
        
        tk.Checkbutton(
            options_frame, 
            text="Uppercase Letters (A-Z)", 
            variable=self.uppercase_var,
            bg='#2c3e50',
            fg='white',
            selectcolor='#34495e',
            font=('Arial', 10)
        ).pack(anchor='w', padx=10, pady=2)
        
        tk.Checkbutton(
            options_frame, 
            text="Lowercase Letters (a-z)", 
            variable=self.lowercase_var,
            bg='#2c3e50',
            fg='white',
            selectcolor='#34495e',
            font=('Arial', 10)
        ).pack(anchor='w', padx=10, pady=2)
        
        tk.Checkbutton(
            options_frame, 
            text="Numbers (0-9)", 
            variable=self.numbers_var,
            bg='#2c3e50',
            fg='white',
            selectcolor='#34495e',
            font=('Arial', 10)
        ).pack(anchor='w', padx=10, pady=2)
        
        tk.Checkbutton(
            options_frame, 
            text="Symbols (!@#$%^&*)", 
            variable=self.symbols_var,
            bg='#2c3e50',
            fg='white',
            selectcolor='#34495e',
            font=('Arial', 10)
        ).pack(anchor='w', padx=10, pady=2)
        
        tk.Checkbutton(
            options_frame, 
            text="Exclude Similar Characters (l, 1, I, O, 0)", 
            variable=self.similar_var,
            bg='#2c3e50',
            fg='white',
            selectcolor='#34495e',
            font=('Arial', 10)
        ).pack(anchor='w', padx=10, pady=2)
        
        tk.Checkbutton(
            options_frame, 
            text="Exclude Ambiguous Characters ({}, [], (), /, \\, |, `, ~)", 
            variable=self.ambiguous_var,
            bg='#2c3e50',
            fg='white',
            selectcolor='#34495e',
            font=('Arial', 10)
        ).pack(anchor='w', padx=10, pady=2)
        
        # Buttons frame
        buttons_frame = tk.Frame(self.window, bg='#2c3e50')
        buttons_frame.pack(pady=20)
        
        # Generate button
        generate_btn = tk.Button(
            buttons_frame,
            text="🔑 Generate Password",
            command=self.generate_password,
            bg='#27ae60',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            relief='flat',
            cursor='hand2'
        )
        generate_btn.pack(side='left', padx=5)
        
        # Copy button
        copy_btn = tk.Button(
            buttons_frame,
            text="📋 Copy to Clipboard",
            command=self.copy_to_clipboard,
            bg='#3498db',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            relief='flat',
            cursor='hand2'
        )
        copy_btn.pack(side='left', padx=5)
        
        # Save button
        save_btn = tk.Button(
            buttons_frame,
            text="💾 Save Password",
            command=self.save_password,
            bg='#f39c12',
            fg='white',
            font=('Arial', 12, 'bold'),
            padx=20,
            pady=10,
            relief='flat',
            cursor='hand2'
        )
        save_btn.pack(side='left', padx=5)
        
        # Password display
        password_frame = tk.LabelFrame(
            self.window, 
            text="Generated Password", 
            bg='#2c3e50', 
            fg='white',
            font=('Arial', 12, 'bold')
        )
        password_frame.pack(pady=10, padx=20, fill='x')
        
        self.password_var = tk.StringVar()
        self.password_entry = tk.Entry(
            password_frame,
            textvariable=self.password_var,
            font=('Courier', 14),
            bg='#34495e',
            fg='#ecf0f1',
            relief='flat',
            state='readonly'
        )
        self.password_entry.pack(pady=10, padx=10, fill='x')
        
        # Password strength indicator
        self.strength_label = tk.Label(
            password_frame,
            text="",
            bg='#2c3e50',
            fg='white',
            font=('Arial', 10)
        )
        self.strength_label.pack(pady=5)
        
        # Saved passwords section
        saved_frame = tk.LabelFrame(
            self.window, 
            text="Saved Passwords", 
            bg='#2c3e50', 
            fg='white',
            font=('Arial', 12, 'bold')
        )
        saved_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Text area for saved passwords
        self.saved_text = scrolledtext.ScrolledText(
            saved_frame,
            height=8,
            bg='#34495e',
            fg='#ecf0f1',
            font=('Courier', 10),
            relief='flat'
        )
        self.saved_text.pack(pady=10, padx=10, fill='both', expand=True)
        
        # Clear saved passwords button
        clear_btn = tk.Button(
            saved_frame,
            text="🗑️ Clear Saved Passwords",
            command=self.clear_saved_passwords,
            bg='#e74c3c',
            fg='white',
            font=('Arial', 10, 'bold'),
            padx=15,
            pady=5,
            relief='flat',
            cursor='hand2'
        )
        clear_btn.pack(pady=5)
        
    def generate_password(self):
        try:
            length = int(self.length_var.get())
            if length < 4:
                messagebox.showerror("Error", "Password length must be at least 4 characters!")
                return
                
            # Build character set based on options
            chars = ""
            
            if self.uppercase_var.get():
                chars += string.ascii_uppercase
            if self.lowercase_var.get():
                chars += string.ascii_lowercase
            if self.numbers_var.get():
                chars += string.digits
            if self.symbols_var.get():
                chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
                
            if not chars:
                messagebox.showerror("Error", "Please select at least one character type!")
                return
                
            # Remove similar characters if requested
            if self.similar_var.get():
                similar_chars = "l1IO0"
                chars = ''.join(c for c in chars if c not in similar_chars)
                
            # Remove ambiguous characters if requested
            if self.ambiguous_var.get():
                ambiguous_chars = "{}[]()/\\|`~"
                chars = ''.join(c for c in chars if c not in ambiguous_chars)
                
            # Generate password
            password = ''.join(random.choice(chars) for _ in range(length))
            self.password_var.set(password)
            
            # Update strength indicator
            self.update_strength_indicator(password)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid password length!")
            
    def update_strength_indicator(self, password):
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        if len(password) >= 12:
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c.islower() for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
            score += 1
            
        if score <= 2:
            strength = "Weak"
            color = "#e74c3c"
        elif score <= 4:
            strength = "Fair"
            color = "#f39c12"
        elif score <= 5:
            strength = "Good"
            color = "#f1c40f"
        else:
            strength = "Strong"
            color = "#27ae60"
            
        self.strength_label.config(
            text=f"Password Strength: {strength}",
            fg=color
        )
        
    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            try:
                pyperclip.copy(password)
                messagebox.showinfo("Success", "Password copied to clipboard!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")
        else:
            messagebox.showwarning("Warning", "No password to copy!")
            
    def save_password(self):
        password = self.password_var.get()
        if not password:
            messagebox.showwarning("Warning", "No password to save!")
            return
            
        # Create a simple dialog for password description
        dialog = tk.Toplevel(self.window)
        dialog.title("Save Password")
        dialog.geometry("300x150")
        dialog.configure(bg='#2c3e50')
        dialog.transient(self.window)
        dialog.grab_set()
        
        tk.Label(dialog, text="Description (optional):", bg='#2c3e50', fg='white').pack(pady=10)
        
        desc_var = tk.StringVar()
        desc_entry = tk.Entry(dialog, textvariable=desc_var, width=30)
        desc_entry.pack(pady=5)
        
        def save():
            description = desc_var.get().strip() or "No description"
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            password_data = {
                "password": password,
                "description": description,
                "timestamp": timestamp,
                "length": len(password)
            }
            
            self.saved_passwords.append(password_data)
            self.save_passwords_to_file()
            self.update_saved_passwords_display()
            dialog.destroy()
            messagebox.showinfo("Success", "Password saved successfully!")
            
        save_btn = tk.Button(
            dialog,
            text="Save",
            command=save,
            bg='#27ae60',
            fg='white',
            padx=20
        )
        save_btn.pack(pady=10)
        
    def load_saved_passwords(self):
        self.saved_passwords = []
        try:
            if os.path.exists('saved_passwords.json'):
                with open('saved_passwords.json', 'r') as f:
                    self.saved_passwords = json.load(f)
        except Exception as e:
            print(f"Error loading saved passwords: {e}")
            
        self.update_saved_passwords_display()
        
    def save_passwords_to_file(self):
        try:
            with open('saved_passwords.json', 'w') as f:
                json.dump(self.saved_passwords, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save passwords: {str(e)}")
            
    def update_saved_passwords_display(self):
        self.saved_text.delete(1.0, tk.END)
        
        if not self.saved_passwords:
            self.saved_text.insert(tk.END, "No saved passwords yet.\n")
            return
            
        for i, pwd_data in enumerate(self.saved_passwords, 1):
            self.saved_text.insert(tk.END, f"{i}. {pwd_data['description']}\n")
            self.saved_text.insert(tk.END, f"   Password: {pwd_data['password']}\n")
            self.saved_text.insert(tk.END, f"   Length: {pwd_data['length']} | Created: {pwd_data['timestamp']}\n")
            self.saved_text.insert(tk.END, "-" * 50 + "\n")
            
    def clear_saved_passwords(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all saved passwords?"):
            self.saved_passwords = []
            self.save_passwords_to_file()
            self.update_saved_passwords_display()
            messagebox.showinfo("Success", "All saved passwords cleared!")
            
    def run(self):
        self.window.mainloop()

def main():
    app = PasswordGenerator()
    app.run()

if __name__ == "__main__":
    main()
