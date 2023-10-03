from enum import Enum

class AccountType(Enum):
    GUEST = 1
    RECEPTIONIST = 2
    HOUSEKEEPING = 3
    SERVER = 4

class Account:
    def __init__(self, username, password, account_type):
        self.username = username
        self.password = password
        self.type = account_type

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_type(self):
        return self.type