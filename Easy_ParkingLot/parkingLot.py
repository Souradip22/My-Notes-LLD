from datetime import datetime
from classes.vehicle import HandicappedVehicle


class ParkingLot:
    def __init__(self, floors, rows, spots_per_row):
        self.floors = floors
        self.rows = rows
        self.spots_per_row = spots_per_row
        self.spots = [[[None for _ in range(spots_per_row)] for _ in range(rows)] for _ in range(floors)]

    def park(self, vehicle, floor, row, spot):
        if self.spots[floor][row][spot] is None:
            self.spots[floor][row][spot] = vehicle
            print(f"{vehicle.get_type()} parked successfully at floor {floor}, row {row}, spot {spot}.")
            return True
        else:
            print("Spot already occupied.")
            return False

    def leave(self, vehicle):

        for i in range(self.floors):
            for j in range(self.rows):
                for k in range(self.spots_per_row):
                    if (self.spots[i][j][k]):
                        print(self.spots[i][j][k].get_no())
                    
                    
                    if self.spots[i][j][k] == vehicle:
                        hours = self.calculate_hours_parked(self.spots[i][j][k], i, j, k)
                        cost = self.spots[i][j][k].calculate_cost(hours)
                        self.spots[i][j][k] = None
                        print(f"{vehicle.get_no()} {vehicle.get_type()} left successfully. Total cost: {cost}")
                        return True
        print(f"{vehicle.get_type()} not found.")
        return False

    def available_spots(self, floor):
        count = 0
        for i in range(self.rows):
            for j in range(self.spots_per_row):
                if self.spots[floor][i][j] is None:
                    count += 1
        return count

    def handicapped_spots(self, floor):
        count = 0
        for i in range(self.rows):
            for j in range(self.spots_per_row):
                if isinstance(self.spots[floor][i][j], HandicappedVehicle):
                    count += 1
        return count

    def calculate_hours_parked(self, vehicle, floor, row, spotId):
        if self.spots[floor][row][spotId] == vehicle:
            now = datetime.now()
            parked_time = self.spots[floor][row][spotId].get_parked_time()

            duration = (now - parked_time).seconds / 3600  # Convert seconds to hours
            return duration
                    
        return 0
