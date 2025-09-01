from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["MovieBot"]
users = db["users"]

def add_user(user_id):
    if not users.find_one({"_id": user_id}):
        users.insert_one({"_id": user_id})
