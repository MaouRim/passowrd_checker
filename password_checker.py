import re

print("\nWelcome to the Password Strength Checker\n")

password = input("Enter your password: ")

strength = 0

print("\nAnalyzing your password...\n")

if len(password) >= 8:
    strength += 1
    print("✔ Good password length")
else:
    print("• Try using at least 8 characters")

if re.search(r"[A-Z]", password):
    strength += 1
    print("✔ Contains uppercase letter")
else:
    print("• Add at least one uppercase letter")

if re.search(r"[a-z]", password):
    strength += 1
    print("✔ Contains lowercase letter")
else:
    print("• Add at least one lowercase letter")

if re.search(r"[0-9]", password):
    strength += 1
    print("✔ Contains a number")
else:
    print("• Add at least one number")

if re.search(r"[^A-Za-z0-9]", password):
    strength += 1
    print("✔ Contains special character")
else:
    print("• Add at least one special character")

print("\nPassword Strength Result:")

if strength <= 2:
    print("Weak Password")
elif strength <= 4:
    print("Medium Password")
else:
    print("Strong Password")

print(f"\nFinal Score: {strength}/5")

