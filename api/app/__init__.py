from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db, SavingsGoal

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        
        
        

    return app