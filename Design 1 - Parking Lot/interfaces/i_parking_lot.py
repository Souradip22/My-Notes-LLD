from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from interfaces.i_vehicle import Vehicle
from models.parking_ticket import ParkingTicket


class IParkingLot(ABC):
    @abstractmethod
    def park_vehicle(self, vehicle: Vehicle) -> ParkingTicket:
        pass

    @abstractmethod
    def unpark_vehicle(self, ticket: ParkingTicket) -> float:
        pass

    @abstractmethod
    def get_available_slots(self) -> List[int]:
        pass

    @abstractmethod
    def get_vehicle_parking_history(self, vehicle: Vehicle) -> List[ParkingTicket]:
        pass

    @abstractmethod
    def get_parking_duration(self, ticket: ParkingTicket) -> datetime:
        pass