from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    from .routes import app as routes

    app.register_blueprint(routes, url_prefix='/')

    from .models import Patient

    create_database(app)

    return app

def create_database(app):
    if not path.exists('api/instance/database.db'):
        with app.app_context():
            db.create_all()
            print("Created Database!")