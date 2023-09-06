import datetime
from collections import deque

# The __ParkingLot is a singleton class that ensures it will have only one active instance at a time
# Both the Entrance and Exit classes use this class to create and close parking tickets
class __ParkingLot(object):
  __instances = None
  
  def __new__(cls):
    if cls.__instances is None:
        cls.__instances = super(__ParkingLot, cls).__new__(cls)
    return cls.__instances

class ParkingLot(metaclass=__ParkingLot):
  def __init__(self, id, name, address, parking_rate, total_slots):
    # Call the name, address, parking_rate elements of the customer in the parking lot from the database
    self.id = id
    self.name = name
    self.address = address
    self.parking_rate = parking_rate

    self.total_slots = total_slots
    self.available_slots = total_slots
    self.occupied_slots = {}
    self.slot_prices = {
        'compact': 20,   # Price per hour for compact cars
        'large': 40,     # Price per hour for large cars
        'motorcycle': 10, # Price per hour for motorcycles
        'handicapped': 30 # Price per hour for handicapped
    }
    self.parked_vehicles_queue = deque(maxlen=total_slots)

    # Create initial entrance and exit hashmaps respectively
    self.entrance = {}
    self.exit = {}

    # Create a hashmap that identifies all currently generated tickets using their ticket number
    self.tickets = {}

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

    def park_vehicle(self, vehicle_type, registration_number):
        if self.available_slots == 0:
            print("Sorry, parking lot is full")
        else:
            # Find the first available slot
            for slot_number in range(1, self.total_slots + 1):
                if slot_number not in self.occupied_slots:
                    entry_time = datetime.datetime.now()
                    self.occupied_slots[slot_number] = {
                        'vehicle_type': vehicle_type,
                        'registration_number': registration_number,
                        'entry_time': entry_time
                    }
                    self.parked_vehicles_queue.appendleft(slot_number)
                    self.available_slots -= 1
                    print(f"Vehicle parked in slot {slot_number}")
                    break


    def unpark_vehicle(self, slot_number):
        if slot_number in self.occupied_slots:
            vehicle_type = self.occupied_slots[slot_number]['vehicle_type']
            registration_number = self.occupied_slots[slot_number]['registration_number']
            entry_time = self.occupied_slots[slot_number]['entry_time']
            exit_time = datetime.datetime.now()
            del self.occupied_slots[slot_number]
            self.available_slots += 1
            print(f"Vehicle unparked from slot {slot_number}")
            return vehicle_type, registration_number, entry_time, exit_time
        else:
            print(f"No vehicle found in slot {slot_number}")
            return None
        

        