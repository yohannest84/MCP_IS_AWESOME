# Flask Application Boilerplate

A modern Flask application template with a clean project structure and best practices implementation.

## Features

- Modular application structure
- SQLAlchemy ORM with migrations support
- Environment-based configuration
- Basic user model
- Type hints throughout the codebase
- Testing setup with pytest
- Basic templates with CSS styling

## Project Structure

```
├── src/                    # Application source code
│   ├── models/            # Database models
│   ├── routes/            # Route handlers
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # Jinja2 templates
│   ├── app.py            # Application factory
│   └── config.py         # Configuration classes
├── tests/                 # Test suite
├── .env.example          # Example environment variables
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and configure your environment variables:
   ```bash
   cp .env.example .env
   ```

4. Initialize the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the development server:
   ```bash
   flask run
   ```

## Testing

Run tests with pytest:
```bash
python -m pytest
```

With coverage report:
```bash
python -m pytest --cov=src
```

## License

This project is licensed under the MIT License.