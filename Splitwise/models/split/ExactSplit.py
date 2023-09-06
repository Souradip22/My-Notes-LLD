from models.split.Split import Split
from models.User import User


class ExactSplit(Split):

    def __init__(self, user: User, amount: float):
        super(ExactSplit, self).__init__(user)
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount



