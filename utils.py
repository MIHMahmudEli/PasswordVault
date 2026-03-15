import string
from storage import StorageManager
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

    @staticmethod
    def is_duplicate(website, username):
        data = StorageManager().load()
        for item in data:
            if item.get("website") == website and item.get("username") == username:
                return True
        return False

class PreventEmptyInput:
    def __init__(self, message):
        self.message = message
    def __call__(self, value):
        if not value:
            raise ValueError(self.message)
