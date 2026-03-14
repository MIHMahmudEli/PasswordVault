class Credential:
    """Entity class representing a single credential entry."""
    def __init__(self, website, username, password, id=None):
        self.id = id
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        """Convert object to dictionary for JSON storage."""
        return {
            "id": self.id,
            "website": self.website,
            "username": self.username,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, data):
        """Create object from dictionary."""
        return cls(
            id=data.get("id"),
            website=data.get("website"),
            username=data.get("username"),
            password=data.get("password")
        )
