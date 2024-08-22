from datetime import datetime
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Mongo:
    def __init__(self):
        # Create a new client and connect to the server
        self.client = MongoClient(
            "mongodb+srv://dorbilia:Db05982005@users.iqmkh.mongodb.net/")
        self.db = self.client["Users"]

    def add_user(self, user_id, password, name, tel_number, email, address, balance):
        self.db.create_collection(user_id)
        document = {
            "_id": int(user_id),
            "password": password,
            "name": name,
            "tel_number": tel_number,
            "email": email,
            "address": address,
            "balance": balance
        }
        self.db[user_id].insert_one(document)

    def add_credit_card(self, user_id, card_number, ccv, secret_code, frame):
        now = datetime.now()
        expiry = datetime.strptime(f"{now.month}/{now.year + 4}", "%m/%Y")
        document = {
            "_id": card_number,
            "expirationDate": expiry,
            "ccv": ccv,
            "secretCode": secret_code,
            "frame": frame,
            "used": 0
        }
        self.db[user_id].insert_one(document)

    def search_info(self, id, information_to_check=None):
        result = self.db[id].find_one(information_to_check)
        return result

    def update_info(self, id, where_to_update, information_to_update):
        update = self.db[id].update_one(where_to_update, {"$set": information_to_update})
        return "'updatedExisting': True" in str(update)

if __name__ == "__main__":
    mongo = Mongo()
    print(mongo.add_user("987654321", "password", "name2", "05412345", "email@mail", "address", 200))
    print(mongo.add_credit_card("987654321", 654321, 321, 321, 100))
    # print(mongo.update_info("12345678", {"_id": 12345}, {"balance": 110}))
