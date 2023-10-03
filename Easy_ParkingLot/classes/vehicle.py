from abc import ABC, abstractmethod
from datetime import datetime, timedelta

from classes.payment import BikePayment, CarPayment, HandicappedPayment

class Vehicle(ABC):
    def __init__(self, regNo):
        self.regNo = regNo
        self.payment = None
        self.parked_time = datetime.now() -  timedelta(hours=3)

    @abstractmethod
    def get_type(self):
        pass

    def calculate_cost(self, hours):
        return self.payment.calculate_cost(hours)

    def set_parked_time(self):
        self.parked_time = datetime.now() - 300000

    def get_parked_time(self):
        return self.parked_time

    def get_no(self):
        return self.regNo

class Car(Vehicle):
    def __init__(self, regNo):
        super().__init__(regNo)
        self.payment = CarPayment()

    def get_type(self):
        return "Car"

class Bike(Vehicle):
    def __init__(self, regNo):
        super().__init__(regNo)
        self.payment = BikePayment()

    def get_type(self):
        return "Bike"

class HandicappedVehicle(Vehicle):
    def __init__(self, regNo):
        super().__init__(regNo)
        self.payment = HandicappedPayment()

    def get_type(self):
        return "Handicapped"