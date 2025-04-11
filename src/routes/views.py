from typing import Union
from flask import render_template, jsonify
from src.routes import main_bp

@main_bp.route('/')
def index() -> str:
    """Handle requests to the root URL.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

@main_bp.route('/health')
def health_check() -> tuple[dict[str, str], int]:
    """Health check endpoint.

    Returns:
        tuple: JSON response with status and HTTP status code.
    """
    return jsonify({'status': 'healthy'}), 200 