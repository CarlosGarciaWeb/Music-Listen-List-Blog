from music_library.routes import pages
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()


def create_app():
    app = Flask(__name__)
    mongo_address = os.getenv("MONGODB_ADDRESS")
    secret_key = os.getenv("SECRET_KEY")
    app.config["MONGO_URI"] = mongo_address
    app.config["SECRET_KEY"] = secret_key
    app.db = MongoClient(app.config["MONGO_URI"]).get_default_database()

    app.register_blueprint(pages)
    return app

