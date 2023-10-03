
from abstract_classes.abc_parking_spot import ParkingSpot
from models.vehicles.handicapped import HandicappedVehicle


class HandicappedSpot(ParkingSpot):
    def __init__(self, id) -> None:
        super().__init__(id)

    def assign_vehicle(self, vehicle):
        if isinstance(vehicle, HandicappedVehicle):  # Check if the vehicle is of the correct type
            self.vehicle = vehicle
        else:
            print("Cannot assign vehicle. Incompatible vehicle type.")
    
    