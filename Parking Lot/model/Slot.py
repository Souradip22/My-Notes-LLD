from model.Car import Car


class Slot:

    parkedCar: Car

    def __init__(self, slotNumber):
        self.slotNumber = slotNumber
        self.parkedCar: Car = None

    def getSlotNumber(self):
        return self.slotNumber

    def getParkedCar(self) -> Car:
        return self.parkedCar

    def isSlotFree(self):
        return self.parkedCar is None

    def assignCar(self, car: Car):
        self.parkedCar = car

    def unassignCar(self):
        self.parkedCar = None

    