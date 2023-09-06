
from models.User import User


class UserService:
    userDetails = {}

    def addUser(self, id, name, email, phone):
        user = User(id, name, email, phone)
        # user.id = id
        # user.name = name
        # user.email = email
        # user.phone = phone

        self.__class__.userDetails[id] = user

        return user
