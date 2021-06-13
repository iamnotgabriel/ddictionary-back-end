from flask_pymongo import PyMongo

from app.config import Mongo


def get_db():
    return mongo


def get_mongo_uri():
    return f"mongodb://{Mongo.HOST}:27017/{Mongo.DB}"


mongo = PyMongo()
