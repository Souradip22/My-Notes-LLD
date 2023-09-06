from controllers.ExpenseController import ExpenseController
from controllers.UserController import UserController
from models.split.EqualSplit import EqualSplit
from services.ExpenseService import ExpenseService
from services.UserService import UserService

userService = UserService()
expenseController = ExpenseController(ExpenseService(), userService)
userController = UserController(userService)

userController.addUser()
userController.addUser("u1", "User1", "gaurav@workat.tech", "9876543210")
userController.addUser("u2", "User2", "sagar@workat.tech", "9876543210")
userController.addUser("u3", "User3", "hi@workat.tech", "9876543210")
userController.addUser("u4", "User4", "mock-interviews@workat.tech", "9876543210")
splits = []
# noOfUsers = 4
# splits.append()
# for i in range(noOfUsers):
#         splits.append(EqualSplit(userService.userDetails.get('U1')))
splits.append(EqualSplit(userService.userDetails.get('u1')))
splits.append(EqualSplit(userService.userDetails.get('u2')))
splits.append(EqualSplit(userService.userDetails.get('u3')))
splits.append(EqualSplit(userService.userDetails.get('u4')))

expenseController.addExpense('EQUAL', 1000, 'u1' , splits, None)
