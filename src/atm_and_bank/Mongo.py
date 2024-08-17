from datetime import datetime
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


class Mongo:
    def __init__(self):
        # Create a new client and connect to the server
        self.client = MongoClient(
            "mongodb+srv://dorbilia:Db05982005@users.iqmkh.mongodb.net/?retryWrites=true&w=majority&appName=Users")
        self.db = self.client["Users"]

    def add_user(self, user_id, password, name, tel_number, email, address, balance):
        try:
            self.db.create_collection(user_id)
            document = {
                "_id": user_id,
                "password": password,
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
        try:
            self.db[user_id].insert_one(document)
            return True
        except:
            return False

    def search_card(self, id, information_to_check):
        print(self.db["dorbili"].find_one({"_id": "123456"}))
        result = self.db[id].find_one(information_to_check)
        if result is not None:
            return result
        return {}


if __name__ == "__main__":
    mongo = Mongo()
    print(mongo.add_user(12345678,"password","name","05412345","email@mail","address",100))
    print(mongo.add_credit_card("dorbili", 123456, 123, 123, 100))
