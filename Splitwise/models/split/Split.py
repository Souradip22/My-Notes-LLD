import abc
from models.User import User


class Split(metaclass=abc.ABCMeta):

    def __init__(self, user: User):
        self.user = user

    def getUser(self):
        return self.user

    def setUser(self, user):
        self.user = user



    # @property
    # def user(self) -> User:
    #     return self.user
    #
    # @user.setter
    # def user(self, value: User):
    #     self.user = value

    # @property
    # def amount(self):
    #     return self.amount
    #
    # @amount.setter
    # def amount(self, value):
    #     self.amount = value
