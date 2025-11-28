import os
from dotenv import load_dotenv  # requires python-dotenv install

load_dotenv()  # loads everything from .env into environment variables


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "replace-with-real-key-during-production"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///" + os.path.join(
        basedir, "app.db"
    )
