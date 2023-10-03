# Example usage
from classes.vehicle import Bike, Car, HandicappedVehicle
from parkingLot import ParkingLot


parking_lot = ParkingLot(floors=3, rows=5, spots_per_row=10)
car = Car("C1")
car2 = Car("C2")
bike = Bike("B1")
bike2 = Bike('B2')
handicapped_vehicle = HandicappedVehicle("H1")

parking_lot.park(car, floor=1, row=2, spot=3)
parking_lot.park(car2, floor=1, row=2, spot=4)
parking_lot.park(bike, floor=0, row=3, spot=7)
parking_lot.park(handicapped_vehicle, floor=2, row=1, spot=0)

parking_lot.park(bike2, floor=2, row=1, spot=1)

parking_lot.leave(bike)

parking_lot.leave(car2)
print(f"Available spots on floor 0: {parking_lot.available_spots(floor=0)}")
print(f"Available spots on floor 1: {parking_lot.available_spots(floor=1)}")
print(f"Available spots on floor 2: {parking_lot.available_spots(floor=2)}")
print(f"Handicapped spots on floor 2: {parking_lot.handicapped_spots(floor=2)}")