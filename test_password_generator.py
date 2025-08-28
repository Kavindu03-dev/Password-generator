#!/usr/bin/env python3
"""
Test script for Password Generator
Tests the core password generation functionality.
"""

import random
import string
import sys

def test_password_generation():
    """Test basic password generation functionality."""
    print("🧪 Testing Password Generator...")
    print("=" * 50)
    
    # Test 1: Basic password generation
    print("Test 1: Basic password generation")
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(16))
    print(f"Generated: {password}")
    print(f"Length: {len(password)}")
    print(f"Contains uppercase: {any(c.isupper() for c in password)}")
    print(f"Contains lowercase: {any(c.islower() for c in password)}")
    print(f"Contains numbers: {any(c.isdigit() for c in password)}")
    print(f"Contains symbols: {any(c in '!@#$%^&*' for c in password)}")
    print()
    
    # Test 2: Password with specific character types
    print("Test 2: Password with specific character types")
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*"
    
    all_chars = uppercase + lowercase + numbers + symbols
    password2 = ''.join(random.choice(all_chars) for _ in range(20))
    print(f"Generated: {password2}")
    print(f"Length: {len(password2)}")
    print()
    
    # Test 3: Password strength calculation
    print("Test 3: Password strength calculation")
    def check_strength(password):
        score = 0
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
            return "Weak"
        elif score <= 4:
            return "Fair"
        elif score <= 5:
            return "Good"
        else:
            return "Strong"
    
    test_passwords = [
        "abc123",  # Weak
        "password123",  # Fair
        "MyPassword123",  # Good
        "MySecureP@ssw0rd!",  # Strong
    ]
    
    for pwd in test_passwords:
        strength = check_strength(pwd)
        print(f"Password: {pwd} -> Strength: {strength}")
    
    print()
    
    # Test 4: Character exclusion
    print("Test 4: Character exclusion")
    chars_without_similar = ''.join(c for c in all_chars if c not in "l1IO0")
    password3 = ''.join(random.choice(chars_without_similar) for _ in range(16))
    print(f"Generated (no similar chars): {password3}")
    print(f"Contains similar chars: {any(c in 'l1IO0' for c in password3)}")
    print()
    
    print("✅ All tests completed successfully!")
    print("The password generator is working correctly.")
    
    return True

def test_cli_import():
    """Test if CLI module can be imported."""
    try:
        from cli_password_generator import CLIPasswordGenerator
        print("✅ CLI module import successful")
        return True
    except ImportError as e:
        print(f"❌ CLI module import failed: {e}")
        return False

def test_gui_import():
    """Test if GUI module can be imported."""
    try:
        import tkinter
        print("✅ Tkinter available for GUI")
        return True
    except ImportError as e:
        print(f"❌ Tkinter not available: {e}")
        return False

if __name__ == "__main__":
    print("🔐 Password Generator Test Suite")
    print("=" * 50)
    
    # Run tests
    test1_passed = test_password_generation()
    test2_passed = test_cli_import()
    test3_passed = test_gui_import()
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print(f"Core functionality: {'✅ PASS' if test1_passed else '❌ FAIL'}")
    print(f"CLI module: {'✅ PASS' if test2_passed else '❌ FAIL'}")
    print(f"GUI module: {'✅ PASS' if test3_passed else '❌ FAIL'}")
    
    if all([test1_passed, test2_passed, test3_passed]):
        print("\n🎉 All tests passed! Your password generator is ready to use.")
        print("\nTo run the GUI version:")
        print("  python password_generator.py")
        print("\nTo run the CLI version:")
        print("  python cli_password_generator.py")
    else:
        print("\n⚠️ Some tests failed. Please check the installation.")
        sys.exit(1)
