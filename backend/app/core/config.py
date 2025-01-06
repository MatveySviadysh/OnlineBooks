from pymongo import MongoClient
import os
from motor.motor_asyncio import AsyncIOMotorClient

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DB_NAME = "fastapi"

config = Config()

client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]

async def get_database():
    client = AsyncIOMotorClient(config.MONGO_URI)
    db = client[config.DB_NAME]
    try:
        yield db
    finally:
        client.close()