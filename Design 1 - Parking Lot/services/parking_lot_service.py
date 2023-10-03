from datetime import datetime
from typing import List

#Models import
from models.parking_lot import ParkingLot


#Export all different spots
from models.parking_spots.handicapped import HandicappedSpot
from models.parking_spots.large import LargeSpot
from models.parking_spots.motorcycle import MotorcycleSpot
from models.parking_spots.compact import CompactSpot


# from models.vehicle import Vehicle

from models.parking_ticket import ParkingTicket
# from interfaces.i_parking_lot import IParkingLot
# from services.payment_service import PaymentService


class ParkingLotService:
    def __init__(self, id, name, address):
        # Create a ParkingLot instance
        print(id, name, address)
        self.parking_lot = ParkingLot(id, name, address)
        # self.total_slots = total_slots
        # self.hourly_rate = hourly_rate
        # self.available_slots = list(range(1, total_slots + 1))
        # self.parking_slots = {}
        # self.payment_service = PaymentService()

    # Method to add Handicapped parking spots
    def add_handicapped_spots(self, count):
        for i in range(count):
            spot_id = f"H{len(self.parking_lot.parking_spots) + 1}"
            handicapped_spot = HandicappedSpot(spot_id)
            self.parking_lot.parking_spots["handicapped"].append(handicapped_spot)

    # Method to add Compact parking spots
    def add_compact_spots(self, count):
        for i in range(count):
            spot_id = f"C{len(self.parking_lot.parking_spots) + 1}"
            compact_spot = CompactSpot(spot_id)
            self.parking_lot.parking_spots["compact"].append(compact_spot)

    # Method to add Large parking spots
    def add_large_spots(self, count):
        for i in range(count):
            spot_id = f"L{len(self.parking_lot.parking_spots) + 1}"
            large_spot = LargeSpot(spot_id)
            self.parking_lot.parking_spots["large"].append(large_spot)

    # Method to add Motorcycle parking spots
    def add_motorcycle_spots(self, count):
        for i in range(count):
            spot_id = f"M{len(self.parking_lot.parking_spots) + 1}"
            motorcycle_spot = MotorcycleSpot(spot_id)
            self.parking_lot.parking_spots["motorcycle"].append(motorcycle_spot)


    # def get_total_spots(self):
    #     return self.parking_lot.get_total_spots()
    

    def get_all_spots(self):
        return self.parking_lot.parking_spots

    
      
    def get_total_spots(self):
        total = 0
        for spot in self.parking_lot.parking_spots:
            total += len(self.parking_lot.parking_spots[spot])
        return total
    
    def get_availeble_spots(self, type):
        return self.parking_lot.calculate_available_slots_by_type(type)

    
    

    # def park_vehicle(self, vehicle_type, registration_number):
    #     if self.available_slots == 0:
    #         print("Sorry, parking lot is full")
    #     else:
    #         # Find the first available slot
    #         for slot_number in range(1, self.total_slots + 1):
    #             if slot_number not in self.occupied_slots:
    #                 entry_time = datetime.datetime.now()
    #                 self.occupied_slots[slot_number] = {
    #                     'vehicle_type': vehicle_type,
    #                     'registration_number': registration_number,
    #                     'entry_time': entry_time
    #                 }
    #                 self.parked_vehicles_queue.appendleft(slot_number)
    #                 self.available_slots -= 1
    #                 print(f"Vehicle parked in slot {slot_number}")
    #                 break


    # def unpark_vehicle(self, slot_number):
    #     if slot_number in self.occupied_slots:
    #         vehicle_type = self.occupied_slots[slot_number]['vehicle_type']
    #         registration_number = self.occupied_slots[slot_number]['registration_number']
    #         entry_time = self.occupied_slots[slot_number]['entry_time']
    #         exit_time = datetime.datetime.now()
    #         del self.occupied_slots[slot_number]
    #         self.available_slots += 1
    #         print(f"Vehicle unparked from slot {slot_number}")
    #         return vehicle_type, registration_number, entry_time, exit_time
    #     else:
    #         print(f"No vehicle found in slot {slot_number}")
    #         return None


    # entrance here refers to an instance of the Entrance class
    def add_entrance(self, entrance):
        pass

    # exit here refers to an instance of the Exit class
    def add_exit(self, exit):
        pass

    # This function allows parking tickets to be available at multiple entrances
    # vehicle here refers to an Vehicle of the Exit class
    # Returns a ParkingTicket instance
    def get_parking_ticket(self, vehicle):
        pass

    # type here refers to an instance of the ParkingSpot class
    def is_full(self, type):
        pass