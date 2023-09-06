

from typing import Optional
from datetime import datetime
from models.payment import Payment
from models.parking_ticket import ParkingTicket
from interfaces.i_payment import IPayment


class PaymentService(IPayment):
    def __init__(self, payment_method: str):
        self.payment_method = payment_method

    def process_payment(self, ticket: ParkingTicket, amount: float) -> Optional[Payment]:
        current_time = datetime.now()
        payment = Payment(ticket, current_time, amount, self.payment_method)
        # Process payment logic here, e.g. sending a request to a payment gateway
        # If payment is successful, return the Payment object, otherwise return None
        if payment_is_successful:
            return payment
        else:
            return None