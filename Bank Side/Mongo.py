from datetime import datetime
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Mongo:
    def __init__(self, connection_string):
        # Create a new client and connect to the server
        self.client = MongoClient(connection_string)
        self.db = self.client["Users"]

    def add_user(self, user_id, name, tel_number, email, address, balance):
        try:
            self.db.create_collection(user_id)
            document = {
                "_id": user_id,
                "name": name,
                "tel_number": tel_number,
                "email": email,
                "address": address,
                "balance": balance
            }
            self.db[user_id].insert_one(document)
            return True
        except:
            return False

    def add_credit_card(self, user_id, card_number, ccv):
        now = datetime.now()
        expiry = now.strftime(f"%m/{now.year + 4}")
        document = {
            "_id": card_number,
            "expirationDate": expiry,
            "ccv": ccv,
        }
        try:
            self.db[user_id].insert_one(document)
            return True
        except:
            return False


if __name__ == "__main__":
    mongo = Mongo(
        "mongodb+srv://dorbilia:Db05982005@users.iqmkh.mongodb.net/?retryWrites=true&w=majority&appName=Users")
    mongo.add_user("dorbili", "Dorbili", 123456, "abc@a", "address", 0)
    mongo.add_credit_card("dorbili", 123, 123)
