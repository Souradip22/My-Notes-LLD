from datetime import datetime
from typing import List
from models.vehicle import Vehicle
from models.parking_ticket import ParkingTicket
from interfaces.i_parking_lot import IParkingLot
from services.payment_service import PaymentService


class ParkingLotService(IParkingLot):
    def __init__(self, total_slots: int, hourly_rate: float):
        self.total_slots = total_slots
        self.hourly_rate = hourly_rate
        self.available_slots = list(range(1, total_slots + 1))
        self.parking_slots = {}
        self.payment_service = PaymentService()

    def park_vehicle(self, vehicle: Vehicle) -> ParkingTicket:
        if not self.available_slots:
            raise Exception("Parking lot is full.")

        parking_slot = self.available_slots.pop(0)
        entry_time = datetime.now()
        ticket = ParkingTicket(vehicle, entry_time)
        ticket.parking_slot = parking_slot
        self.parking_slots[parking_slot] = ticket

        return ticket

    def unpark_vehicle(self, ticket: ParkingTicket) -> float:
        parking_slot = ticket.parking_slot
        del self.parking_slots[parking_slot]
        self.available_slots.append(parking_slot)

        exit_time = datetime.now()
        ticket.exit_time = exit_time
        duration = self.get_parking_duration(ticket)
        parking_fee = duration.total_seconds() / 3600 * self.hourly_rate
        ticket.parking_fee = parking_fee

        self.payment_service.process_payment(parking_fee)

        return parking_fee

    def get_available_slots(self) -> List[int]:
        return self.available_slots

    def get_vehicle_parking_history(self, vehicle: Vehicle) -> List[ParkingTicket]:
        return [ticket for ticket in self.parking_slots.values() if ticket.vehicle == vehicle]

    def get_parking_duration(self, ticket: ParkingTicket) -> datetime:
        return ticket.exit_time - ticket.entry_time