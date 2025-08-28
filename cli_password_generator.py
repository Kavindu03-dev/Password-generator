#!/usr/bin/env python3
"""
Command Line Password Generator
A simple and secure password generator for terminal use.
"""

import argparse
import random
import string
import json
import os
from datetime import datetime

class CLIPasswordGenerator:
    def __init__(self):
        self.saved_passwords_file = 'cli_saved_passwords.json'
        self.load_saved_passwords()
        
    def load_saved_passwords(self):
        """Load saved passwords from JSON file."""
        self.saved_passwords = []
        try:
            if os.path.exists(self.saved_passwords_file):
                with open(self.saved_passwords_file, 'r') as f:
                    self.saved_passwords = json.load(f)
        except Exception as e:
            print(f"Warning: Could not load saved passwords: {e}")
            
    def save_passwords_to_file(self):
        """Save passwords to JSON file."""
        try:
            with open(self.saved_passwords_file, 'w') as f:
                json.dump(self.saved_passwords, f, indent=2)
        except Exception as e:
            print(f"Error saving passwords: {e}")
            
    def generate_password(self, length=16, uppercase=True, lowercase=True, 
                         numbers=True, symbols=True, exclude_similar=False, 
                         exclude_ambiguous=False):
        """Generate a password with specified criteria."""
        
        # Build character set
        chars = ""
        
        if uppercase:
            chars += string.ascii_uppercase
        if lowercase:
            chars += string.ascii_lowercase
        if numbers:
            chars += string.digits
        if symbols:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
            
        if not chars:
            raise ValueError("At least one character type must be selected!")
            
        # Remove similar characters if requested
        if exclude_similar:
            similar_chars = "l1IO0"
            chars = ''.join(c for c in chars if c not in similar_chars)
            
        # Remove ambiguous characters if requested
        if exclude_ambiguous:
            ambiguous_chars = "{}[]()/\\|`~"
            chars = ''.join(c for c in chars if c not in ambiguous_chars)
            
        # Generate password
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
        
    def check_password_strength(self, password):
        """Check password strength and return score and feedback."""
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
        elif score <= 4:
            strength = "Fair"
        elif score <= 5:
            strength = "Good"
        else:
            strength = "Strong"
            
        return strength, score
        
    def save_password(self, password, description=""):
        """Save password with description."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        password_data = {
            "password": password,
            "description": description or "No description",
            "timestamp": timestamp,
            "length": len(password)
        }
        
        self.saved_passwords.append(password_data)
        self.save_passwords_to_file()
        print(f"✅ Password saved successfully!")
        
    def list_saved_passwords(self):
        """Display all saved passwords."""
        if not self.saved_passwords:
            print("📝 No saved passwords found.")
            return
            
        print("\n📋 Saved Passwords:")
        print("=" * 60)
        
        for i, pwd_data in enumerate(self.saved_passwords, 1):
            print(f"{i}. {pwd_data['description']}")
            print(f"   Password: {pwd_data['password']}")
            print(f"   Length: {pwd_data['length']} | Created: {pwd_data['timestamp']}")
            print("-" * 60)
            
    def clear_saved_passwords(self):
        """Clear all saved passwords."""
        if self.saved_passwords:
            self.saved_passwords = []
            self.save_passwords_to_file()
            print("🗑️ All saved passwords cleared!")
        else:
            print("📝 No saved passwords to clear.")
            
    def interactive_mode(self):
        """Run interactive mode for password generation."""
        print("🔐 Interactive Password Generator")
        print("=" * 40)
        
        while True:
            print("\nOptions:")
            print("1. Generate password")
            print("2. List saved passwords")
            print("3. Clear saved passwords")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                self.interactive_generate()
            elif choice == '2':
                self.list_saved_passwords()
            elif choice == '3':
                confirm = input("Are you sure? (y/N): ").strip().lower()
                if confirm == 'y':
                    self.clear_saved_passwords()
            elif choice == '4':
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")
                
    def interactive_generate(self):
        """Interactive password generation with user input."""
        print("\n🔑 Password Generation Options:")
        
        # Get length
        while True:
            try:
                length = int(input("Password length (4-128, default 16): ").strip() or "16")
                if 4 <= length <= 128:
                    break
                else:
                    print("❌ Length must be between 4 and 128.")
            except ValueError:
                print("❌ Please enter a valid number.")
                
        # Get character options
        print("\nCharacter types (y/n):")
        uppercase = input("Uppercase letters (A-Z)? (Y/n): ").strip().lower() != 'n'
        lowercase = input("Lowercase letters (a-z)? (Y/n): ").strip().lower() != 'n'
        numbers = input("Numbers (0-9)? (Y/n): ").strip().lower() != 'n'
        symbols = input("Symbols (!@#$%^&*)? (Y/n): ").strip().lower() != 'n'
        
        # Get exclusion options
        print("\nExclusion options (y/n):")
        exclude_similar = input("Exclude similar characters (l, 1, I, O, 0)? (y/N): ").strip().lower() == 'y'
        exclude_ambiguous = input("Exclude ambiguous characters ({}, [], (), /, \\, |, `, ~)? (y/N): ").strip().lower() == 'y'
        
        try:
            password = self.generate_password(
                length=length,
                uppercase=uppercase,
                lowercase=lowercase,
                numbers=numbers,
                symbols=symbols,
                exclude_similar=exclude_similar,
                exclude_ambiguous=exclude_ambiguous
            )
            
            strength, score = self.check_password_strength(password)
            
            print(f"\n🔐 Generated Password: {password}")
            print(f"📊 Strength: {strength} (Score: {score}/6)")
            print(f"📏 Length: {len(password)}")
            
            # Ask if user wants to save
            save = input("\n💾 Save this password? (y/N): ").strip().lower()
            if save == 'y':
                description = input("Description (optional): ").strip()
                self.save_password(password, description)
                
        except ValueError as e:
            print(f"❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Generate secure passwords from the command line",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                    # Interactive mode
  %(prog)s -l 20             # Generate 20-character password
  %(prog)s -l 12 --no-symbols # Generate 12-char password without symbols
  %(prog)s --list            # List saved passwords
  %(prog)s --clear           # Clear saved passwords
        """
    )
    
    parser.add_argument('-l', '--length', type=int, default=16,
                       help='Password length (default: 16)')
    parser.add_argument('--no-uppercase', action='store_true',
                       help='Exclude uppercase letters')
    parser.add_argument('--no-lowercase', action='store_true',
                       help='Exclude lowercase letters')
    parser.add_argument('--no-numbers', action='store_true',
                       help='Exclude numbers')
    parser.add_argument('--no-symbols', action='store_true',
                       help='Exclude symbols')
    parser.add_argument('--exclude-similar', action='store_true',
                       help='Exclude similar characters (l, 1, I, O, 0)')
    parser.add_argument('--exclude-ambiguous', action='store_true',
                       help='Exclude ambiguous characters ({}, [], (), /, \\, |, `, ~)')
    parser.add_argument('--save', action='store_true',
                       help='Save generated password')
    parser.add_argument('--description', type=str, default='',
                       help='Description for saved password')
    parser.add_argument('--list', action='store_true',
                       help='List saved passwords')
    parser.add_argument('--clear', action='store_true',
                       help='Clear all saved passwords')
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run in interactive mode')
    
    args = parser.parse_args()
    
    generator = CLIPasswordGenerator()
    
    # Handle special commands
    if args.list:
        generator.list_saved_passwords()
        return
    elif args.clear:
        generator.clear_saved_passwords()
        return
    elif args.interactive or len([arg for arg in vars(args).values() if arg]) == 0:
        generator.interactive_mode()
        return
        
    # Generate password with specified options
    try:
        password = generator.generate_password(
            length=args.length,
            uppercase=not args.no_uppercase,
            lowercase=not args.no_lowercase,
            numbers=not args.no_numbers,
            symbols=not args.no_symbols,
            exclude_similar=args.exclude_similar,
            exclude_ambiguous=args.exclude_ambiguous
        )
        
        strength, score = generator.check_password_strength(password)
        
        print(f"🔐 Generated Password: {password}")
        print(f"📊 Strength: {strength} (Score: {score}/6)")
        print(f"📏 Length: {len(password)}")
        
        if args.save:
            generator.save_password(password, args.description)
            
    except ValueError as e:
        print(f"❌ Error: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())
