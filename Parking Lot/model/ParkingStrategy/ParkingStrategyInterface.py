import abc


class ParkingStrategyInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def addSlot(self, slotNumber):
        pass

    @abc.abstractmethod
    def removeSlot(self, slotNumber):
        pass

    @abc.abstractmethod
    def getNextSlot(self):
        pass

