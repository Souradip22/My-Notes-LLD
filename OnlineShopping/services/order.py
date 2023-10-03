class Order:
    def __init__(self, customer, products, total_cost, payment, shipping):
        self.customer = customer
        self.products = products
        self.total_cost = total_cost
        self.payment = payment
        self.shipping = shipping

    # getters and setters
    def get_customer(self):
        return self.customer

    def get_products(self):
        return self.products

    def get_total_cost(self):
        return self.total_cost

    def get_payment(self):
        return self.payment

    def get_shipping(self):
        return self.shipping

    def set_customer(self, customer):
        self.customer = customer

    def set_products(self, products):
        self.products = products

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    def set_payment(self, payment):
        self.payment = payment

    def set_shipping(self, shipping):
        self.shipping = shipping

    # operator overloading for comparing two orders
    def __eq__(self, other):
        return (self.customer == other.customer and self.products == other.products and self.total_cost == other.total_cost)