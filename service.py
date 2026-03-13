import string
import random

class PasswordService:
    
    def add_password(self, website, username, password):
        print("Add a Password called")
        
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
