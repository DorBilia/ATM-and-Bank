class User:
    def __init__(self, id, password, name, tel_number, email, address, balance):
        self.id = id
        self.password = password
        self.name = name
        self.tel_number = tel_number
        self.email = email
        self.address = address
        self.balance = balance

    def change_balance(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def get_email(self):
        return self.email
