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

    def get_passwords(self):
        data = self.storage.load()
        return data

    def search_password(self, query):
        """Search credentials by website or username."""
        all_pass = self.get_passwords()
        results = []
        for p in all_pass:
            if query.lower() in p.get('website', '').lower() or query.lower() in p.get('username', '').lower():
                results.append(p)
        return results
        
    
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
