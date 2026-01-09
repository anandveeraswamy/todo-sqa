from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = "auth.login"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Development shortcut only to create tables if they do not exist
    # For Production use: flask db init       # only once per project
    # flask db migrate -m "Initial tables"
    # flask db upgrade

    with app.app_context():
        db.create_all()

    # Register blueprints
    from app import auth, tasks, main

    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)
    app.register_blueprint(main.bp)

    # init_routes(app)

    return app
