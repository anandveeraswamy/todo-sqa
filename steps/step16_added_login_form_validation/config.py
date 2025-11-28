import os
from dotenv import load_dotenv # requires python-dotenv install
load_dotenv()  # loads everything from .env into environment variables


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'replace-with-real-key-during-production'