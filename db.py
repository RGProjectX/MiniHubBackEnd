from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


client = MongoClient('mongodb+srv://rohit:rohit@cluster0.3xmfspx.mongodb.net/?retryWrites=true&w=majority')
db = client['minihub']
user_collection = db['users']
project_collection = db['projects']
