from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Initialize database globally so it can be imported elsewhere
db = SQLAlchemy()

def create_app():
    """Flask application factory pattern."""
    load_dotenv()

    app = Flask(__name__)

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Initialize extensions
    db.init_app(app)

    # Import routes (if in a separate file)
    from . import routes
    app.register_blueprint(routes.bp)

    return app
