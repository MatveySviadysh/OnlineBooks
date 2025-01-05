from pymongo import MongoClient
import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = "fastapi"

config = Config()

client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]
