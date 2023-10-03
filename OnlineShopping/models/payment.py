class Payment:
    def __init__(self, amount=0, payment_method=""):
        self.amount = amount
        self.payment_method = payment_method

    # getters and setters
    def get_amount(self):
        return self.amount

    def get_payment_method(self):
        return self.payment_method

    def set_amount(self, amount):
        self.amount = amount

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    # payment method functions
    def pay_with_credit_card(self):
        # code to process credit card payment
        pass

    def pay_with_debit_card(self):
        # code to process debit card payment
        pass

    def pay_with_net_banking(self):
        # code to process net banking payment
        pass