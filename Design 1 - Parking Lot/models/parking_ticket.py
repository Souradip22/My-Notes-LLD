class ParkingTicket:
    def __init__(self, ticket_no, timestamp, exit, amount, status, vehicle, payment, entrance, exit_ins) -> None:
        self.ticket_no = ticket_no
        self.timestamp = timestamp
        self.exit = exit
        self.amount = amount
        self.status = status
        
        # Following are the instances of their respective classes
        self.vehicle = vehicle
        self.payment = payment
        self.entrance = entrance
        self.exit_ins = exit_ins