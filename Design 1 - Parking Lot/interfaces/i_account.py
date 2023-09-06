
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, user_name, password, person, status) -> None:
        self.user_name = user_name
        self.password = password
        self.person = person # Refers to the person class
        self.status = status # refer tp the account state enum

    @abstractmethod
    def reset_password(self):
        pass