from controllers.ExpenseController import ExpenseController
from controllers.UserController import UserController
from models.split.ExactSplit import ExactSplit
from services.ExpenseService import ExpenseService
from services.UserService import UserService

userService = UserService()
expenseController = ExpenseController(ExpenseService(), userService)
userController = UserController(userService)

userController.addUser("u1", "User1", "gaurav@workat.tech", "9876543210")
userController.addUser("u2", "User2", "sagar@workat.tech", "9876543210")
userController.addUser("u3", "User3", "hi@workat.tech", "9876543210")
userController.addUser("u4", "User4", "mock-interviews@workat.tech", "9876543210")
splits = []
# Input: EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
# Input: EXPENSE u1 1250 2 u2 u3 EXACT 370 880
# Input: EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
# Input: SHOW (show all balances)


userInput = input("Enter Command Type, paid by, amount, no_of_users, users and expense type separated by space:").split()
commandType = userInput[0]


if commandType == 'SHOW':
    if len(userInput) == 1:
        # show all the users output
        expenseController.showBalances()
    else:
        # show user input for a particular user
        userId = userInput[1]
        expenseController.showBalance(userId)

if commandType == 'EXPENSE':
    paidBy = userInput[1]
    amount = float(userInput[2])
    noOfUser = int(userInput[3])
    users = list(userInput[4: 4 + noOfUser])
    expenseType = userInput[4 + noOfUser]
    print(paidBy, amount, noOfUser, users, expenseType)




print(userInput)
# noOfUsers = 4
# splits.append()
# for i in range(noOfUsers):
#         splits.append(EqualSplit(userService.userDetails.get('U1')))
# splits.append(EqualSplit(userService.userDetails.get('u1')))
# splits.append(EqualSplit(userService.userDetails.get('u2')))
# splits.append(EqualSplit(userService.userDetails.get('u3')))
# splits.append(EqualSplit(userService.userDetails.get('u4')))

splits.append(ExactSplit(userService.userDetails.get('u2'), 370))
splits.append(ExactSplit(userService.userDetails.get('u3'), 880))

print(splits)

expenseController.addExpense('EXACT', 1250, 'u1', splits, None)

# expenseController.showBalance('u2')
expenseController.showBalances()

