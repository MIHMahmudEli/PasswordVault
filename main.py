from ui import PasswordVaultUI

def main():
    """Main entry point of the application."""
    app = PasswordVaultUI()
    
    try:
        app.display_menu()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Stay safe!")
        
if __name__ == "__main__":
    main()