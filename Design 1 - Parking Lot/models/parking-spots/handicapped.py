
from interfaces.i_parking_spot import ParkingSpot


class Handicapped(ParkingSpot):
    def __init__(self, id, isFree, vehicle) -> None:
        super().__init__(id, isFree, vehicle)

    def assign_vehicle(self, vehicle):
        return super().assign_vehicle(vehicle)
    
    