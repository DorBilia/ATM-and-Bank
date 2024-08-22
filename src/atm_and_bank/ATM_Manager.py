import Mongo
from datetime import datetime


class ATM_Manager:
    def __init__(self):
        self.mongo = Mongo.Mongo()

    def login(self, id, credit_card, ccv, month, year):
        date_str = f"{month}/{year}"
        date_format = '%m/%Y'
        inputs_to_check = {"_id": int(credit_card),
                           "expirationDate": datetime.strptime(date_str, date_format),
                           "ccv": int(ccv)}
        return [self.mongo.search_info(id), self.mongo.search_info(id, inputs_to_check)]
        # first value - the user's details
        # second value - the user's credit_card
    def send_money(self,other_account):