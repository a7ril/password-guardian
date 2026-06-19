from password_checker import PasswordChecker
from password_generator import PasswordGenerator
import os
from colorama import init, Fore, Style
init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_check(label, value):
    if value:
        print(Fore.GREEN + f"{label}: Yes")
    else:
        print(Fore.RED + f"{label}: No")


while True:
    clear_screen()
    print(Fore.BLUE + "*" * 30)
    print(Fore.CYAN + "      Password Guardian")
    print(Fore.BLUE + "*" * 30)
    print("1- Check password strength")
    print("-" * 30)
    print("2- Generate a strong password")
    print("-" * 30)
    print("3- Check multiple passwords")
    print("-" * 30)
    print("4- Generate multiple passwords")
    print("-" * 30)
    print("5- Exit")
    print("-" * 30)

    choice = input("Choose an option: ")

    if choice == "1":
        pwd = input("Enter the password to check: ")

        if pwd == "":
            print("Password cannot be empty!")
        else:
            checker = PasswordChecker(pwd)
            print(f"Strength: {checker.get_strength()}")
            print_check("Length >= 8", checker.is_strong())
            print_check("Has uppercase", checker.has_uppercase())
            print_check("Has lowercase", checker.has_lowercase())
            print_check("Has digit", checker.has_digit())
            print_check(
                "Has special character", checker.has_special_char())

    elif choice == "2":
        length_input = input(
            "Enter desired password length (or press Enter for default): ")

        if length_input == "":
            gen = PasswordGenerator()
        else:
            length = int(length_input)
            gen = PasswordGenerator(length)

        new_password = gen.generate()
        print(f"Generated Password: {new_password}")
    elif choice == "3":
        passwords_input = input("Enter passwords separated by commas: ")
        password_list = passwords_input.split(",")

        for pwd in password_list:
            pwd = pwd.strip()
            checker = PasswordChecker(pwd)
            print(f"{pwd} --> {checker.get_strength()}")

    elif choice == "4":
        count_input = input("How many passwords do you want to generate? ")
        count = int(count_input)

        gen = PasswordGenerator()

        for i in range(count):
            print(gen.generate())

    elif choice == "5":
        print("Goodluck!")
        break

    else:
        print("Invalid option, please try again.")
