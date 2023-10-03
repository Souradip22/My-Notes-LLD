#Import different service
from services.parking_lot_service import ParkingLotService

# Example usage of the ParkingLotService
if __name__ == "__main__":
    print('inside main')
    parking_service = ParkingLotService(1, "My Parking Lot", "123 Main St.")
    # parking_service2 = ParkingLotService(2, "My Parking Lot", "123 Main St.") # Test to see if singleton class working properly


    parking_service.add_handicapped_spots(5)
    parking_service.add_compact_spots(6)
    parking_service.add_large_spots(4)
    parking_service.add_motorcycle_spots(3)


    print("Toatal Spots", parking_service.get_total_spots())
    print("Toatal Spots", parking_service.get_availeble_spots('compact'))
    # print("Get all spots", parking_service.get_all_spots())

    # Add parking spots
    # parking_service.add_parking_spots(5, 10, 8, 15)

    # Park a vehicle
    # car_ticket = parking_service.park_vehicle("car", "ABC123")

    # Simulate parking duration...

    # Exit the vehicle
    # final_fee = parking_service.exit_vehicle(car_ticket)
    # print(f"Final Parking Fee for Car: ${final_fee}")