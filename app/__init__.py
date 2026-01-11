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

    # instructions to initialise the db
    # For Production use: flask db init       # only once per project
    # flask db migrate -m "Initial tables"
    # flask db upgrade

    # Import models to register them with SQLAlchemy
    from app.auth import models as auth_models  # noqa: F401
    from app.tasks import models as task_models  # noqa: F401

    # Register blueprints
    from app import auth, tasks, main

    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)
    app.register_blueprint(main.bp)

    return app
