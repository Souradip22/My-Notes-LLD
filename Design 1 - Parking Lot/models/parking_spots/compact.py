
from abstract_classes.abc_parking_spot import ParkingSpot
from models.vehicles.car import CarVehicle
from models.vehicles.van import VanVehicle


class CompactSpot(ParkingSpot):
    def __init__(self, id) -> None:
        super().__init__(id)

    def assign_vehicle(self, vehicle):
        if isinstance(vehicle, CarVehicle):  # Check if the vehicle is of the correct type
            self.vehicle = vehicle
        else:
            print("Cannot assign vehicle. Incompatible vehicle type.")
    
    