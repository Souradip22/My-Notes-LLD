from interfaces.i_vehicle import Vehicle


class MotorcycleVehicle(Vehicle):
    def __init__(self, license_no) -> None:
        super().__init__(license_no)

    def assign_ticket(self, ticket):
        return super().assign_ticket(ticket)
    