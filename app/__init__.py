from flask import Flask
from flask_cors import CORS
from config import Config

def create_app(config_class=Config):
    """Application factory pattern"""
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Enable CORS
    CORS(app)
    
    # Register blueprints
    from app.routes import user_routes
    app.register_blueprint(user_routes.bp)
    
    return app

