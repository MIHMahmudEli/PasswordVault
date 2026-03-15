import string
import random
from storage import StorageManager
from models import Credential
from crypto_manager import CryptoManager

class PasswordService:
    def __init__(self):
        """Service class for managing password operations and business logic."""
        self.storage = StorageManager()
        self.crypto = CryptoManager()

    #add password method
    def add_password(self, website, username, password):
        """Create and add a new credential."""
        data = self.storage.load()
        new_id = max([item.get("id", 0) for item in data], default=0) + 1
        encrypted_password = self.crypto.encrypt(password)
        new_entry = Credential(website, username, encrypted_password, id=new_id)
        data.append(new_entry.to_dict())
        return self.storage.save(data)

    #get all passwords method
    def get_passwords(self):
        data = self.storage.load()
        for item in data:
            item["password"] = self.crypto.decrypt(item["password"])
        return data

    #search password method
    def search_password(self, query):
        """Search credentials by ID."""
        all_creds = self.get_passwords()
        return [c for c in all_creds if query.lower() in c["username"] or query.lower() in c["website"] or str(c["id"]) == query]


    #generate password method
    def generate_secure_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

        
    #delete password method
    def delete_password(self, id):
        """Delete a credential by ID."""
        data = self.storage.load()
        updated_data = [item for item in data if item.get("id") != id]
        if len(data) == len(updated_data):
            return False
        return self.storage.save(updated_data)

    #update password method
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
                    encrypted_password = self.crypto.encrypt(password)
                    item["password"] = encrypted_password
                return self.storage.save(data)
        return False

    #view summary report method
    def view_summary_report(self):
        """Calculate summary statistics."""
        data = self.storage.load()
        total_accounts = len(data)
        websites = set(item.get("website") for item in data)
        return {
            "total_entries": total_accounts,
            "unique_websites": len(websites)
        }
        

