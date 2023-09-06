from exception.InvalidSlotException import InvalidSlotException
from exception.ParkingLotException import ParkingLotException
from exception.SlotAlreadyOccupiedException import SlotAlreadyOccupiedException
from model.Car import Car
from model.Slot import Slot


class ParkingLot:
    MAX_CAPACITY = 10000

    def __init__(self, capacity):

        if (capacity > self.__class__.MAX_CAPACITY) or (capacity <= 0):
            raise ParkingLotException("Invalid capacity given for parking lot.")

        self.capacity = capacity
        self.slots = {}

    def getSlots(self):
        return self.slots

    def getCapacity(self):
        return self.capacity

    def getSlot(self, slotNumber):
        if (slotNumber > self.getCapacity()) or (slotNumber <= 0):
            raise InvalidSlotException()

        allSlots = self.getSlots()

        if not allSlots.get(slotNumber):
            allSlots[slotNumber] = Slot(slotNumber)

        return allSlots.get(slotNumber)

    def park(self, car: Car, slotNumber: int):
        slot: Slot = self.getSlot(slotNumber)
        if not slot.isSlotFree():
            raise SlotAlreadyOccupiedException()
        slot.assignCar(car)
        return slot

    def makeSlotFree(self, slotNumber: int):
        slot: Slot = self.getSlot(slotNumber)
        slot.unassignCar()
        return slot
