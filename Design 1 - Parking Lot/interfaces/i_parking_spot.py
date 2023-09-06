from abc import ABC, abstractmethod

class ParkingSpot(ABC):
    def __init__(self, id, isFree, vehicle) -> None:
        self.id = id
        self.isFree = isFree
        self.vehicle = vehicle #referes to an instance of vehicle class

    def get_is_free(self):
        pass

    @abstractmethod
    def assign_vehicle(self, vehicle):
        pass

    def remove_vehicle(self):
        pass

        