from flask import Blueprint

main_bp = Blueprint('main', __name__)

from src.routes import views  # noqa: E402 