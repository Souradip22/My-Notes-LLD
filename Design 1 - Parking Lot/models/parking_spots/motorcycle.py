
from abstract_classes.abc_parking_spot import ParkingSpot
from models.vehicles.motorcycle import MotorcycleVehicle

class MotorcycleSpot(ParkingSpot):
    def __init__(self, id) -> None:
        super().__init__(id)

    def assign_vehicle(self, vehicle):
        if isinstance(vehicle, MotorcycleVehicle):  # Check if the vehicle is of the correct type
            self.vehicle = vehicle
        else:
            print("Cannot assign vehicle. Incompatible vehicle type.")
    