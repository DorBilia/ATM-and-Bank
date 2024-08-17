import Mongo
import ATM_Login
from datetime import datetime


class Run_ATM:
    def __init__(self):
        self.mongo = Mongo.Mongo()

    def login(self, id, credit_card, ccv, month, year):
        date_str = f"{month}/{year}"
        date_format = '%m/%Y'
        inputs_to_check = {"_id": int(credit_card),
                           "expirationDate": datetime.strptime(date_str, date_format),
                           "ccv": int(ccv)}
        # print(inputs_to_check)
        return self.mongo.search_card(id, inputs_to_check)
