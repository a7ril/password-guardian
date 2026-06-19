class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def is_strong(self):
        return len(self.password) >= 8

    def has_uppercase(self):
        for char in self.password:
            if char.isupper():
                return True
        return False

    def has_lowercase(self):
        for char in self.password:
            if char.islower():
                return True
        return False

    def has_digit(self):
        for char in self.password:
            if char.isdigit():
                return True
        return False

    def has_special_char(self):
        special_characters = "!@#$%^&*()_-=+"
        for char in self.password:
            if char in special_characters:
                return True
        return False

    def get_strength(self):
        score = 0

        if self.is_strong():
            score += 1
        if self.has_uppercase():
            score += 1
        if self.has_lowercase():
            score += 1
        if self.has_digit():
            score += 1
        if self.has_special_char():
            score += 1

        if score == 5:
            return "Very Strong"
        elif score >= 3:
            return "Medium"
        else:
            return "Weak"
