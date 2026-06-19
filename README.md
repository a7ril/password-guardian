# Password Guardian

A command-line Python tool to check password strength and generate strong random passwords. Built as a learning project while studying Python and cybersecurity fundamentals.

## What it does

It can check password strength, looking at length, uppercase, lowercase, digits, and special characters, with a color-coded breakdown (green for pass, red for fail). It can also generate a random strong password with a customizable length, and check or generate multiple passwords at once.

## Project structure

The project is organized into separate classes, each with a single responsibility.

`password_checker.py` contains the `PasswordChecker` class, which evaluates password strength. `password_generator.py` contains the `PasswordGenerator` class, which generates random strong passwords. `main.py` is the interactive menu that ties everything together.

## Technologies used

Python 3, and the colorama library for colored terminal output. The password generator also uses Python’s built-in random and string modules to generate passwords.

## How to run it

Clone the repository, install the dependency, and run the program:

```bash
git clone https://github.com/your-username/password-guardian.git
cd password-guardian
pip install colorama
python main.py
```

Then follow the on-screen menu to check or generate passwords.

## Example

```
Choose an option: 1
Enter the password to check: MyPassword123!
Strength: Very Strong
Length >= 8: Yes
Has uppercase: Yes
Has lowercase: Yes
Has digit: Yes
Has special character: Yes
```

Each line is color-coded, green when the check passes and red when it fails, so the results are easy to scan.

## What I learned

This project was built step by step as a hands-on introduction to Python classes and object-oriented design, loops and conditional logic, string manipulation and validation, working with external libraries like colorama, and designing a simple command-line interface.

## Possible next steps

Saving password check history to a file, checking passwords against a list of known leaked passwords, and maybe building a GUI version.

## Author

Built by Shouq as part of an ongoing journey into Python and cybersecurity.

