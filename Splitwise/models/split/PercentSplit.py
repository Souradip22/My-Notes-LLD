from models.split.Split import Split
from models.User import User


class PercentSplit(Split):
    def __init__(self, user: User, percent):
        super(PercentSplit, self).__init__(user)
        self.percent = percent

    def getPercent(self):
        return self.percent

    def setPercent(self, percent):
        self.percent = percent
