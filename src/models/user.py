from datetime import datetime
from src.app import db

class User(db.Model):
    """User model for storing user related details.

    Attributes:
        id: Primary key for the user.
        username: Unique username for the user.
        email: Unique email address of the user.
        password: User's password (should be hashed in production).
        created_at: Timestamp of when the user was created.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        """String representation of the User model.

        Returns:
            str: String containing the username.
        """
        return f'<User {self.username}>' 