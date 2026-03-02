from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    
    CORS(app)
    
    from app.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    
    return app
