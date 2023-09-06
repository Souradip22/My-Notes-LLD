from controllers.ExpenseController import ExpenseController
from services.UserService import UserService


class UserController(object):

	def __init__(self, userService: UserService):
		self.userService = userService

	def addUser(self, id, name, email, phone):
		ExpenseController.balanceSheet[id] = {}
		return self.userService.addUser(id, name, email, phone)