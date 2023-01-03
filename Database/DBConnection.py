from pymongo import MongoClient


class DBConnection:
    def __init__(self, mongoDBConnectionString, database, collection):
        client = MongoClient(mongoDBConnectionString)
        db = client[database]
        self.collection = db[collection]
