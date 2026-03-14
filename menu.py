from ui import PasswordVaultUI
from colorama import Fore, Style, init
import sys

# Initialize colorama
init(autoreset=True)    

class Menu(PasswordVaultUI):
    def display_header(self):
        print(Fore.CYAN + "=" * 50)
        print(Fore.LIGHTWHITE_EX + "       🔐 SECURE PASSWORD VAULT CLI 🔐")
        print(Fore.CYAN + "=" * 50)
        
    def display_menu(self):
        while True:
            self.display_header()
            print("1. " + Fore.GREEN + "Add a new password" + Style.RESET_ALL)
            print("2. " + Fore.BLUE + "View all passwords" + Style.RESET_ALL)
            print("3. " + Fore.BLUE + "Search for a password" + Style.RESET_ALL)
            print("4. " + Fore.YELLOW + "Generate a password" + Style.RESET_ALL)
            print("5. " + Fore.RED + "Delete a password" + Style.RESET_ALL)
            print("6. " + Fore.MAGENTA + "Update a password" + Style.RESET_ALL)
            print("7. " + Fore.MAGENTA + "View summary report" + Style.RESET_ALL)
            print("0. " + Fore.RED + "Exit" + Style.RESET_ALL)
            
            choice = input("\nChoose an option: ")
            
            match choice:   
                case '1':
                    self.add_password()
                case '2':
                    self.get_passwords()
                case '3':
                    self.search_password()
                case '4':
                    self.generate_password()
                case '5':
                    self.delete_password()
                case '6':
                    self.update_password()
                case '7':
                    self.view_summary_report()
                case '0':
                    print(Fore.GREEN + "Thank you for using the Password Vault!" + Style.RESET_ALL)
                    sys.exit()
                case _:
                    print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)