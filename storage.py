import json

class StorageManager:
    """Storage class for handling JSON data persistence."""
    def __init__(self, file_path="passwords.json"):
        self.file_path = file_path
        
    def save(self, data):
        """Save a list of dictionaries to a JSON file."""
        try:
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False
        

        
    
    
    