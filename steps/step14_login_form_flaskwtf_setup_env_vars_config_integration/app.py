from flask import Flask
from config import Config


app = Flask(__name__)
# loads all uppercase attributes from the Config class into the Flask application's configuration
app.config.from_object(Config) 
import routes
