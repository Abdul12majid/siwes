#password
import random

class PasswordGenerator:
    def __init__(self, password_length=12, symbols=True, numbers=True, uppercase=True, lowercase=True):
        self.password_length = password_length
        self.symbols = symbols
        self.numbers = numbers
        self.uppercase = uppercase
        self.lowercase = lowercase

        self.password_characters = ""
        if self.symbols:
            self.password_characters += "!@#$%^&*()_+"
        if self.numbers:
            self.password_characters += "0123456789"
        if self.uppercase:
            self.password_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.lowercase:
            self.password_characters += "abcdefghijklmnopqrstuvwxyz"

    def generate_password(self):
        password = ""
        for i in range(self.password_length):
            password += random.choice(self.password_characters)

        return password


def main():
    password_generator = PasswordGenerator()

    print("Your generated password is:", password_generator.generate_password())

    # Ask the user if they want to generate another password
    while True:
        generate_again = input("Generate another password? (y/n): ")
        if generate_again == "y":
            password_generator = PasswordGenerator()
            print("Your generated password is:", password_generator.generate_password())
        elif generate_again == "n":
            break
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
