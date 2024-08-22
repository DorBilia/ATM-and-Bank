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

    def send_money(self, sender_account, sender_credit_card, receiver_account_id, amount):
        sender_account_id = sender_account.get("_id")
        other_account_info = self.mongo.search_info(receiver_account_id)
        try:
            self.mongo.update_info(receiver_account_id, {"_id": int(receiver_account_id)},
                                   {"balance": other_account_info.get("balance") + amount})
            self.mongo.update_info(str(sender_account_id), {"_id": int(sender_account_id)},
                                   {"balance": sender_account.get("balance") - amount})
            self.mongo.update_info(str(sender_account_id), {"_id": sender_credit_card.get("_id")},
                                   {"used": sender_credit_card.get("used") + amount})
            return True
        except:
            return False

    def validate_account(self, id):
        return self.mongo.search_info(id)
