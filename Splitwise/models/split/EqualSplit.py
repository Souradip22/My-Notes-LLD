from models.split.Split import Split
from models.User import User


class EqualSplit(Split):

    def __init__(self, user: User):
        super(EqualSplit, self).__init__(user)
