import sys
from colorama import Fore, Style, init
from tabulate import tabulate
from service import PasswordService

# Initialize colorama
init(autoreset=True)

class PasswordVaultUI:
    def __init__(self):
        self.service = PasswordService()
    
    
    def display_header(self):
        print(Fore.CYAN + Style.BRIGHT + "Welcome to the Password Vault!" + Style.RESET_ALL)
        print(Fore.YELLOW + "Your secure place to store and manage your passwords." + Style.RESET_ALL)
        print("-" * 50)
        
    def display_menu(self):
        while True:
            self.display_header()
            print("1. " + Fore.GREEN + "Add a new password" + Style.RESET_ALL)
            print("2. " + Fore.BLUE + "View all passwords" + Style.RESET_ALL)
            print("3. " + Fore.BLUE + "Search for a password" + Style.RESET_ALL)
            print("4. " + Fore.YELLOW + "Generate a password" + Style.RESET_ALL)
            print("5. " + Fore.RED + "Delete a password" + Style.RESET_ALL)
            print("6. " + Fore.MAGENTA + "View summary report" + Style.RESET_ALL)
            print("0. " + Fore.RED + "Exit" + Style.RESET_ALL)
            
            choice = input("\nChoose an option: ")
            
            match choice:   
                case '1':
                    self.add_password()
                case '2':
                    self.view_passwords()
                case '3':
                    self.search_password()
                case '4':
                    self.generate_password()
                case '5':
                    self.delete_password()
                case '6':
                    self.view_summary_report()
                case '0':
                    print(Fore.GREEN + "Thank you for using the Password Vault!" + Style.RESET_ALL)
                    sys.exit()
                case _:
                    print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
    
    def add_password(self):
        self.service.add_password()
    def view_passwords(self):
        self.service.view_passwords()
    def search_password(self):
        self.service.search_password()
    def generate_password(self):
        self.service.generate_password()
    def delete_password(self):
        self.service.delete_password()
    def view_summary_report(self):
        self.service.view_summary_report()
    

