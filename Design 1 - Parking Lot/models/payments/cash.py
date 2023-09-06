from interfaces.i_payment import Payment


class Cash(Payment):
    def __init__(self, amount, status, timestamp):
        super().__init__(amount, status, timestamp)

    def initiate_transaction(self):
        pass

