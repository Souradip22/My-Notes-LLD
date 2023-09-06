class Car:

    def __init__(self, registrationNumber: str, color: str):
        self.color = color
        self.registrationNumber = registrationNumber

    def getColor(self):
        return self.color

    def getRegistrationNumber(self):
        return self.registrationNumber
