from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #sqalchemy usage

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes

        db.create_all()  # Create the database tables if they don't exist

    return app

