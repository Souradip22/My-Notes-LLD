import abc

from models.expense.ExpenseMetaData import ExpenseMetaData
from models.split.Split import Split
from models.User import User


class Expense(metaclass=abc.ABCMeta):

    def __init__(self,  amount: float, paidBy: User, splits: list[Split], expenseMetaData: ExpenseMetaData):
        self.amount = amount
        self.paidBy = paidBy
        self.splits = splits
        self.expenseMetaData = expenseMetaData
        self.id = None

    # subclass of this class need to override this method
    @abc.abstractmethod
    def validate(self):
        pass

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getAmount(self):
        return self.amount

    def setAmount(self, amount):
        self.amount = amount

    def getPaidBy(self):
        return self.paidBy

    def setPaidBy(self, paidBy):
        self.paidBy = paidBy

    def getSplits(self):
        return self.splits

    def setSplits(self, splits):
        self.splits = splits

    def getExpenseMetaData(self):
        return self.expenseMetaData

    def setExpenseMetaData(self, expenseMetaData):
        self.expenseMetaData = expenseMetaData

