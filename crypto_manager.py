import random
import string
import secrets
from cryptography.fernet import Fernet
import os

class CryptoManager:
    def __init__(self, key_path="secret.key"):
        self.key_path = key_path
        self.key = self._load_or_generate_key()
        self.fernet = Fernet(self.key)
    
    def _load_or_generate_key(self):
        """Load the encryption key or generate a new one."""
        if os.path.exists(self.key_path):
            with open(self.key_path, "rb") as key_file:
                return key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_path, "wb") as key_file:
                key_file.write(key)
            return key

    def encrypt(self, text):
        return self.fernet.encrypt(text.encode()).decode()

    def decrypt(self, encrypted_text):
        try:
            return self.fernet.decrypt(encrypted_text.encode()).decode()
        except:
            return "[Decryption Error]"