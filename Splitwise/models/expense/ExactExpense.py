from models.split.ExactSplit import ExactSplit
from models.expense.Expense import Expense
from models.expense.ExpenseMetaData import ExpenseMetaData
from models.split.Split import Split
from models.User import User


class ExactExpense(Expense):
    def __init__(self, amount: float, paidBy: User, splits: list[Split], expenseMetaData: ExpenseMetaData):
        super(ExactExpense, self).__init__(amount, paidBy, splits, expenseMetaData)

    # @override
    def validate(self):
        totalAmount: float = self.amount
        splitSum = 0

        for split in self.splits:
            if not isinstance(split, ExactSplit):
                return False
            exactSplit: ExactSplit = split
            splitSum += exactSplit.amount

        if splitSum != totalAmount:
            return False
        return True
