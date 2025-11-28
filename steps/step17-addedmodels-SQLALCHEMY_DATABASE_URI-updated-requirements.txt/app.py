from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
# loads all uppercase attributes from the Config class into the Flask application's configuration
app.config.from_object(Config) 
db = SQLAlchemy(app)
migrate = Migrate(app, db)
import routes
