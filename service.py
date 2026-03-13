import string
import random
from storage import StorageManager

class PasswordService:
    def __init__(self):
        self.storage = StorageManager()

    def add_password(self, website, username, password):
        """Create and add a new credential."""
        data = {
            "website": website,
            "username": username,
            "password": password
        }
        return self.storage.save([data])

    def view_passwords(self):
        print("View all password called")
        
    def search_password(self):
        print("Search All Password called")
    
    def generate_password(self):
        print("Generate a password called")
        
    def delete_password(self):
        print("Delete Password Callded")
    
    def view_summary_report(self):
        print("View summary Report called")
        
    def generate_secure_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
