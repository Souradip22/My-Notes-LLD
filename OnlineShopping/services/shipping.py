class Shipping:
    def __init__(self, shipping_method="", shipping_cost=0.0):
        self.shipping_method = shipping_method
        self.shipping_cost = shipping_cost

    # getters and setters
    def get_shipping_method(self):
        return self.shipping_method

    def get_shipping_cost(self):
        return self.shipping_cost

    def set_shipping_method(self, shipping_method):
        self.shipping_method = shipping_method

    def set_shipping_cost(self, shipping_cost):
        self.shipping_cost = shipping_cost