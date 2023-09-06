from models.split.EqualSplit import EqualSplit
from models.expense.Expense import Expense
from models.expense.ExpenseMetaData import ExpenseMetaData
from models.split.Split import Split
from models.User import User


class EqualExpense(Expense):
    def __init__(self, amount: float, paidBy: User, splits: list[Split], expenseMetaData: ExpenseMetaData):
        super(EqualExpense, self).__init__(amount, paidBy, splits, expenseMetaData)

    # @override
    def validate(self):
        for split in self.splits:
            if not isinstance(split, EqualSplit):
                return False
        return True



