import sys
from colorama import Fore, Style, init
from tabulate import tabulate
from service import PasswordService
from utils import Utils

# Initialize colorama
init(autoreset=True)

class PasswordVaultUI:
    def __init__(self):
        self.service = PasswordService()
    
    #add password method
    def add_password(self):
        print(Fore.YELLOW + "\n--- Add New Password ---")
        
        website = input("Website Name: ").strip()
        username = input("Username/Email: ").strip()
        
        #duplicate check
        if Utils.is_duplicate(website, username):
            print(Fore.RED + "Credential already exists.")
            return
        
        if not website or not username:
            print(Fore.RED + "Website and Username cannot be empty.")
            return

        #password input
        print("Press Enter to use a generated password, or type your own.")
        while True:
            password = input(Fore.BLUE + "Password: ").strip()
            if not password or Utils.get_password_strength(password) == 5:
                break
            print(Fore.RED + "Password must be at least 8 characters, and contain at least one uppercase, lowercase, number, and special character.")

        if not password:
            password = self.service.generate_secure_password()
            print(Fore.GREEN + f"Generated Password: {password}")

        if self.service.add_password(website, username, password):
            print(Fore.GREEN + "Password saved successfully!")
        else:
            print(Fore.RED + "Failed to save password.")
            
    
    #view password method
    def get_passwords(self):
        data = self.service.get_passwords()

        if not data:
            print(Fore.YELLOW + "\nNo credentials stored yet.")
            return
        
        table = [[entry["id"], entry["website"], entry["username"], entry["password"]] for entry in data]
        print("\n" + tabulate(table, headers=["ID", "Website", "Username/Email", "Password"], tablefmt="fancy_grid"))   
           
    #search password method
    def search_password(self):
        query = input("\nEnter search term ID: ").strip()
        if not query:
            return
        
        results = self.service.search_password(query)
        if not results:
            print(Fore.RED + "No results found.")
            return
        
        table = [[entry["id"], entry["website"], entry["username"], entry["password"]] for entry in results]
        print("\n" + tabulate(table, headers=["ID", "Website", "Username/Email", "Password"], tablefmt="fancy_grid"))   

    #generate password method    
    def generate_password(self):
        try:
            length = input("Enter password length (default 16): ").strip()
            length = int(length) if length else 16
            pwd = self.service.generate_secure_password(length)
            print(Fore.GREEN + f"\nGenerated Password: {pwd}")
        except ValueError:
            print(Fore.RED + "Invalid length. Using default 16.")
            pwd = self.service.generate_secure_password(16)
            print(Fore.GREEN + f"Generated Password: {pwd}")

    #delete password method
    def delete_password(self):
        try:
            id = int(input("\nEnter Credential ID to delete: "))
            if self.service.delete_password(id):
                print(Fore.GREEN + f"Credential {id} deleted.")
            else:
                print(Fore.RED + "Credential ID not found.")
        except ValueError:
            print(Fore.RED + "Invalid ID.")

    #update password method
    def update_password(self):
        try:
            id = int(input("Enter Credential ID to update: "))

            #check if id exists
            if not self.service.search_password(str(id)):
                print(Fore.RED + "Credential ID not found.")
                return
            

            print(Fore.YELLOW + "Leave fields blank if you do not want to change them.")
            website = input(Fore.BLUE + "New Website Name: ").strip()
            username = input(Fore.BLUE + "New Username/Email: ").strip()
            while True:
                password = input(Fore.BLUE + "New Password: ").strip()
                if not password or Utils.get_password_strength(password) == 5:
                    break
                print(Fore.RED + "Password must be at least 8 characters, and contain at least one uppercase, lowercase, number, and special character.")
            
            if self.service.update_password(id, website, username, password):
                print(Fore.GREEN + f"Credential {id} updated.")
            else:
                print(Fore.RED + "Credential ID not found.")
        except ValueError:
            print(Fore.RED + "Invalid ID.")

    #view summary report method
    def view_summary_report(self):
        total_passwords = self.service.view_summary_report()
        print(Fore.GREEN + f"\nTotal Passwords: {total_passwords}")
        
