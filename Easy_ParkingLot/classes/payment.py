from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def calculate_cost(self, hours):
        pass

class CarPayment(Payment):
    def calculate_cost(self, hours):
        return hours * 2

class BikePayment(Payment):
    def calculate_cost(self, hours):
        return hours * 1

class HandicappedPayment(Payment):
    def calculate_cost(self, hours):
        return 0