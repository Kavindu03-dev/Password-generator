# 🔐 Password Generator Pro

A comprehensive password generator application built with Python, featuring both a modern GUI interface and a powerful command-line tool.

## ✨ Features

### GUI Application (`password_generator.py`)
- 🎨 **Modern Dark Theme UI** - Beautiful and easy on the eyes
- 🔧 **Customizable Options** - Control password length and character types
- 📊 **Real-time Strength Analysis** - Visual password strength indicator
- 📋 **One-click Copy** - Copy passwords to clipboard instantly
- 💾 **Password Storage** - Save passwords with descriptions
- 🗑️ **Password Management** - View and clear saved passwords
- 🔒 **Security Options** - Exclude similar/ambiguous characters

### Command Line Tool (`cli_password_generator.py`)
- ⚡ **Fast Generation** - Quick password generation from terminal
- 🎯 **Interactive Mode** - Step-by-step password creation
- 📝 **Batch Operations** - Generate multiple passwords
- 💾 **Local Storage** - Save passwords with timestamps
- 🔍 **Password Listing** - View all saved passwords
- 🗑️ **Cleanup Tools** - Clear saved passwords

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Setup
1. **Clone or download** this project to your local machine
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### GUI Application

Run the graphical interface:
```bash
python password_generator.py
```

**Features:**
- Set password length (4-128 characters)
- Choose character types:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Symbols (!@#$%^&*)
- Exclude similar characters (l, 1, I, O, 0)
- Exclude ambiguous characters ({}, [], (), /, \, |, `, ~)
- Real-time password strength analysis
- Copy to clipboard functionality
- Save passwords with descriptions

### Command Line Tool

#### Interactive Mode
```bash
python cli_password_generator.py
# or
python cli_password_generator.py --interactive
```

#### Quick Generation
```bash
# Generate a 16-character password (default)
python cli_password_generator.py

# Generate a 20-character password
python cli_password_generator.py -l 20

# Generate password without symbols
python cli_password_generator.py --no-symbols

# Generate password with specific options
python cli_password_generator.py -l 12 --no-uppercase --exclude-similar
```

#### Password Management
```bash
# List all saved passwords
python cli_password_generator.py --list

# Clear all saved passwords
python cli_password_generator.py --clear

# Save generated password
python cli_password_generator.py -l 16 --save --description "My website"
```

## 🎯 Examples

### GUI Examples
1. **Strong Password**: 16 characters with all character types
2. **Simple Password**: 8 characters, letters and numbers only
3. **Secure Password**: 24 characters, exclude similar characters

### CLI Examples
```bash
# Generate a strong password for a website
python cli_password_generator.py -l 20 --save --description "Gmail account"

# Generate a simple PIN-like password
python cli_password_generator.py -l 6 --no-uppercase --no-symbols

# Generate a password excluding confusing characters
python cli_password_generator.py -l 16 --exclude-similar --exclude-ambiguous
```

## 🔧 Configuration

### Password Strength Criteria
The application evaluates password strength based on:
- **Length**: 8+ characters (1 point), 12+ characters (1 point)
- **Character Types**: Uppercase, lowercase, numbers, symbols (1 point each)
- **Total Score**: 6 points maximum
- **Strength Levels**:
  - Weak (0-2 points)
  - Fair (3-4 points)
  - Good (5 points)
  - Strong (6 points)

### File Storage
- **GUI Passwords**: Saved in `saved_passwords.json`
- **CLI Passwords**: Saved in `cli_saved_passwords.json`
- **Format**: JSON with password, description, timestamp, and length

## 🛡️ Security Features

- **Cryptographically Secure**: Uses Python's `random` module
- **Character Exclusion**: Option to exclude confusing characters
- **Local Storage**: Passwords stored locally, not transmitted
- **No Logging**: Passwords are not logged or stored in system logs

## 📁 Project Structure

```
Password gen/
├── password_generator.py      # GUI application
├── cli_password_generator.py  # Command-line tool
├── requirements.txt           # Python dependencies
├── README.md                 # This file
├── saved_passwords.json      # GUI saved passwords (created automatically)
└── cli_saved_passwords.json  # CLI saved passwords (created automatically)
```

## 🐛 Troubleshooting

### Common Issues

1. **Import Error for pyperclip**
   ```bash
   pip install pyperclip
   ```

2. **GUI Not Starting**
   - Ensure tkinter is installed (usually included with Python)
   - On Linux: `sudo apt-get install python3-tk`

3. **Clipboard Not Working**
   - Windows: No additional setup required
   - macOS: May need to grant clipboard permissions
   - Linux: May need `xclip` or `xsel`: `sudo apt-get install xclip`

### Error Messages
- **"At least one character type must be selected"**: Check at least one character type checkbox
- **"Password length must be at least 4 characters"**: Increase the length value
- **"Failed to copy to clipboard"**: Check clipboard permissions or install required tools

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Improving the UI/UX
- Adding new password generation algorithms

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This tool is for educational and personal use. Always follow your organization's password policies and security guidelines. The developers are not responsible for any security issues arising from the use of generated passwords.

---

**Happy Password Generating! 🔐✨**
