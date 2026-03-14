import string
class Utils:
    @staticmethod
    def get_password_strength(password):
        strength = 0
        if len(password) >= 8:
            strength += 1
        if any(char.isdigit() for char in password):
            strength += 1
        if any(char.isupper() for char in password):
            strength += 1
        if any(char.islower() for char in password):
            strength += 1
        if any(char in string.punctuation for char in password):
            strength += 1
        return strength
