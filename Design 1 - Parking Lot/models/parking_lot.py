import datetime
from collections import deque
from abstract_classes.abc_parking_spot import ParkingSpot
# The __ParkingLot is a singleton class that ensures it will have only one active instance at a time
# Both the Entrance and Exit classes use this class to create and close parking tickets
class ParkingLotMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(ParkingLotMeta, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class ParkingLot(metaclass=ParkingLotMeta):
  def __init__(self, id, name, address):
      print('init')
      self.id = id
      self.name = name
      self.address = address
  
      
      self.slot_prices = {
          'compact': 20,   # Price per hour for compact cars
          'large': 40,     # Price per hour for large cars
          'motorcycle': 10, # Price per hour for motorcycles
          'handicapped': 30 # Price per hour for handicapped
      }
      # self.parked_vehicles_queue = deque(maxlen=total_spots)

      # Create initial entrance and exit hashmaps respectively
      self.entrance = {}
      self.exit = {}
      # Create a hashmap that identifies all currently generated tickets using their ticket number
      self.tickets = {}
      self.parking_spots = {
          "compact" :[],
          "handicapped":[],
          "large":[],
          "motorcycle":[]
      }
      self.occupied_slots = {}

  def calculate_available_slots_by_type(self, slot_type):
        total_available = 0
        for spot in self.parking_spots[slot_type]:
            if isinstance(spot, ParkingSpot):
                if spot.get_is_free():
                  total_available += 1
        return total_available

  def calculate_occupied_slots(self):
      total_occupied = sum(len(spots) - 1 for spots in self.parking_spots.values())
      return total_occupied

  def park_vehicle(self, vehicle_type, registration_number, slot_type):
      if self.calculate_available_slots_by_type(slot_type) == 0:
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
    
  




  
        

        