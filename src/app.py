from typing import Optional
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class: Optional[type] = None) -> Flask:
    """Create and configure the Flask application.

    Args:
        config_class: Optional configuration class to use. Defaults to Config.

    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    app.config.from_object(config_class or Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from src.routes import main_bp
    app.register_blueprint(main_bp)

    return app 