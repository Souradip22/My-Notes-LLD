from models.expense.Expense import Expense
from models.expense.ExpenseMetaData import ExpenseMetaData
from models.split.PercentSplit import PercentSplit
from models.split.Split import Split
from models.User import User


class PercentExpense(Expense):
    def __init__(self, amount: float, paidBy: User, splits: list[Split], expenseMetaData: ExpenseMetaData):
        super(PercentExpense, self).__init__(amount, paidBy, splits, expenseMetaData)

    # @override
    def validate(self):
        totalAmount = 100
        splitSum = 0

        for split in self.splits:
            if not isinstance(split, PercentSplit):
                return False
            percentSplit: PercentSplit = split
            splitSum += percentSplit.percent

        if splitSum != totalAmount:
            return False
        return True
