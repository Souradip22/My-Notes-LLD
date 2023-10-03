class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product, stock):
        self.products[product] = stock

    def update_stock(self, product, stock):
        self.products[product] = stock

    def is_in_stock(self, product):
        return self.products.get(product, 0) > 0

    def restock(self, product, quantity):
        self.products[product] = self.products.get(product, 0) + quantity