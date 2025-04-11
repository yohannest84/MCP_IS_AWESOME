import os
from typing import Optional

class Config:
    """Application configuration class.

    Attributes:
        SECRET_KEY: Secret key for session management and security.
        SQLALCHEMY_DATABASE_URI: Database connection URI.
        SQLALCHEMY_TRACK_MODIFICATIONS: SQLAlchemy event tracking flag.
    """
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'dev-key-please-change'
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False 