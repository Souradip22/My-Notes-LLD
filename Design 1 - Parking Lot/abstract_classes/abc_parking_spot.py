from abc import ABC, abstractmethod

class ParkingSpot(ABC):
    def __init__(self, spot_id) -> None:
        self.spot_id = spot_id
        self.is_free = True
        self.vehicle = None

    @abstractmethod
    def assign_vehicle(self, vehicle): #4 different spot should call this method to assign vehicle of different types
        pass

    def remove_vehicle(self):
        self.is_free = True
        self.vehicle = None

    def get_is_free(self):
        return self.is_free

        