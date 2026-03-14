from ui import Menu

def main():
    """Main entry point of the application."""
    app = Menu()
    
    try:
        app.display_menu()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user. Stay safe!")
        
if __name__ == "__main__":
    main()