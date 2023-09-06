from models.expense.EqualExpense import EqualExpense
from models.expense.ExactExpense import ExactExpense
from models.expense.ExpenseMetaData import ExpenseMetaData
from models.ExpenseType import ExpenseType
from models.expense.PercentExpense import PercentExpense
from models.split.PercentSplit import PercentSplit
from models.split.Split import Split
from models.User import User


class ExpenseService:
    expenseDetails: list = []

    @staticmethod
    def createExpense(expenseType: ExpenseType, amount: float, paidBy: User, splits: list[Split],
                      expenseMetaData: ExpenseMetaData):
        if expenseType == ExpenseType.EXACT.name:
            return ExactExpense(amount, paidBy, splits, expenseMetaData)

        elif expenseType == ExpenseType.EQUAL.name:
            totalSplits = len(splits)
            splitAmount = (round(amount * 100 / totalSplits)) / 100
            for split in splits:
                eachSplit: Split = split
                eachSplit.amount = splitAmount
            splits[0].setAmount(splitAmount + (amount - splitAmount * totalSplits));
            return EqualExpense(amount, paidBy, splits, expenseMetaData);

        elif expenseType == ExpenseType.PERCENT.name:
            for split in splits:
                percentSplit: PercentSplit = split
                split.amount = (amount * percentSplit) / 100
            return PercentExpense(amount, paidBy, splits, expenseMetaData)
        else:
            return None
