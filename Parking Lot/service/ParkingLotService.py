from exception.ParkingLotException import ParkingLotException
from model.Car import Car
from model.ParkingLot import ParkingLot
from model.ParkingStrategy.ParkingStrategyInterface import ParkingStrategyInterface
from model.Slot import Slot


class ParkingLotService:
    parkingLot: ParkingLot = None
    parkingStrategy: ParkingStrategyInterface = None

    @staticmethod
    def createParkingLot(parkingLot: ParkingLot, parkingStrategy: ParkingStrategyInterface):
        if ParkingLotService.parkingLot is not None:
            raise ParkingLotException("Parking lot already exists.")
        ParkingLotService.parkingLot = parkingLot
        ParkingLotService.parkingStrategy = parkingStrategy
        for i in range(1, parkingLot.getCapacity() + 1):
            ParkingLotService.parkingStrategy.addSlot(i)

    @staticmethod
    def validateParkingLotExists():
        if ParkingLotService.parkingLot is None:
            raise ParkingLotException("parking lot does not exists to park")

    @staticmethod
    def park(car: Car):
        ParkingLotService.validateParkingLotExists()
        nextFreeSlot = ParkingLotService.parkingStrategy.getNextSlot()
        ParkingLotService.parkingLot.park(car, nextFreeSlot)
        ParkingLotService.parkingStrategy.removeSlot(nextFreeSlot)
        return nextFreeSlot

    @staticmethod
    def makeSlotFree(slotNumber: int):
        ParkingLotService.validateParkingLotExists()
        ParkingLotService.parkingLot.makeSlotFree(slotNumber)
        ParkingLotService.parkingStrategy.addSlot(slotNumber)

    @staticmethod
    def getOccupiedSlots():
        ParkingLotService.validateParkingLotExists()
        occupiedSlotsList = []
        allSlots = ParkingLotService.parkingLot.getSlots()

        for i in range(1, ParkingLotService.parkingLot.getCapacity() + 1):
            if allSlots.get(i):
                slot: Slot = allSlots.get(i)
                if not slot.isSlotFree():
                    occupiedSlotsList.append(slot)
        return occupiedSlotsList

    @staticmethod
    def getSlotsForColor(color: str):
        occupiedSlots = ParkingLotService.getOccupiedSlots()
        filtered = filter(lambda slot: color == slot.getParkedCar().getColor(), occupiedSlots)
        return list(filtered)
