import string
import random
from storage import StorageManager
from models import Credential

class PasswordService:
    def __init__(self):
        """Service class for managing password operations and business logic."""
        self.storage = StorageManager()

    def add_password(self, website, username, password):
        """Create and add a new credential."""
        data = self.storage.load()
        new_id = max([item.get("id", 0) for item in data], default=0) + 1
        
        new_entry = Credential(website, username, password, id=new_id)
        data.append(new_entry.to_dict())
        return self.storage.save(data)

    def get_passwords(self):
        data = self.storage.load()
        return data

    def search_password(self, query):
        """Search credentials by ID."""
        all_creds = self.get_passwords()

        return [c for c in all_creds if query.lower() in str(c["id"])]

        
    def delete_password(self, id):
        """Delete a credential by ID."""
        data = self.storage.load()
        updated_data = [item for item in data if item.get("id") != id]
        if len(data) == len(updated_data):
            return False
        return self.storage.save(updated_data)

    def update_password(self, id, website, username, password):
        """Update a credential by ID."""
        data = self.storage.load()
        for item in data:
            if item.get("id") == id:
                if website:
                    item["website"] = website
                if username:
                    item["username"] = username
                if password:
                    item["password"] = password
                return self.storage.save(data)
        return False

    def view_summary_report(self):
        print("View summary Report called")
        
    def generate_secure_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
