import random
import string


class PasswordGenerator:
    def __init__(self, length=12):
        self.length = length

    def generate(self):
        characters = string.ascii_uppercase + \
            string.ascii_lowercase + string.digits + "!@#$%^&*()_-"
        password = ""

        for i in range(self.length):
            password += random.choice(characters)

        return password
