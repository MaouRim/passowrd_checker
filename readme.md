# Password Strength Checker

This is a simple Python project that checks how strong a password is.

The program analyzes a password using basic security rules like:

* password length
* uppercase letters
* lowercase letters
* numbers
* special characters

After checking these conditions, it tells the user whether the password is:

* Weak
* Medium
* Strong

## Why I Built This

I created this project to practice:

* Python fundamentals
* Regular Expressions (Regex)
* Conditional statements
* User input handling
* Basic cybersecurity concepts

## Features

* Checks password strength
* Gives suggestions to improve weak passwords
* Beginner-friendly and easy to understand
* Uses Python regex for validation

## Technologies Used

* Python
* `re` module (Regular Expressions)

## How to Run the Project

Clone the repository:

```bash id="x5m2rp"
git clone https://github.com/MaouRim/passowrd_checker
```

Run the program:

```bash id="w8n4qa"
python password_checker.py
```

## Example

```text id="d6k9vt"
Enter your password: Hello@123

✔ Good password length
✔ Contains uppercase letter
✔ Contains lowercase letter
✔ Contains a number
✔ Contains special character

Strong Password
Final Score: 5/5
```

## What I Learned

Through this project, I learned:

* How password validation works
* How to use regex in Python
* How to build simple command-line applications
* How password strength is calculated

## Future Improvements

Some features I plan to add later:

* Password generator
* GUI version using Tkinter
* Colored terminal output
* Password breach detection
* Entropy-based scoring
