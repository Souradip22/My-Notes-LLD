from models.User import User
from services.ExpenseService import ExpenseService
from services.UserService import UserService


class ExpenseController:
    balanceSheet = {}

    def __init__(self, expenseService: ExpenseService, userService: UserService):
        self.expenseService = expenseService
        self.userService = userService

    def addExpense(self, expenseType, amount, paidBy, splits, expenseMetaData):
        expense = self.expenseService.createExpense(expenseType, amount, paidBy, splits, expenseMetaData)
        if not expense.validate():
            return False
        self.expenseService.expenseDetails.append(expense)
        for split in expense.splits:
            paidTo = split.user.id
            balances = self.__class__.balanceSheet.get(paidBy)
            if not balances.get(paidTo):
                balances[paidTo] = 0.0

            balances[paidTo] = balances.get(paidTo) + split.amount

            balances = self.__class__.balanceSheet.get(paidTo);
            if not balances.get(paidBy):
                balances[paidBy] = 0.0

            balances[paidBy] = balances.get(paidBy) - split.amount

    def showBalance(self, userId: str):
        isEmpty = True
        userBalance = self.__class__.balanceSheet.get(userId, {}).items()
        print('Balance Sheet',self.__class__.balanceSheet, userId, userBalance)
        for userId2, balance in userBalance:
            if balance != 0:
                isEmpty = False
                print(userId, balance)
                self.printBalance(userId, userId2, balance)
                # print(userId, userBalance.keys(), userBalance.values())
        if isEmpty:
            print('No Balances')

    def showBalances(self):
        allBalances = self.__class__.balanceSheet.items()
        print(allBalances)
        for user, balance in allBalances:
            isEmpty = True
            if len(balance.items()):
                isEmpty = False
                for other, otherBalance in balance.items():
                    self.printBalance(user, other, otherBalance)
            # print('--', user, len(balance.items()))
            if isEmpty:
                print(f'No Balance : {user}')

    def printBalance(self, user1: str, user2: str, amount: float):
        user1: User = self.userService.userDetails.get(user1)
        user2: User = self.userService.userDetails.get(user2)
        print(user1.name, user2.name, amount)
        if amount < 0:
            print(f'{user1.name} owes {user2.name} : ${amount}')
        elif amount > 0:
            print(f'{user2.name} owes {user1.name} : ${amount}')
