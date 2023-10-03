from models.inventory import Inventory


class Admin:
    def __init__(self):
        self.inventory = Inventory()
        self.products = []
        self.customers = []
        self.orders = []

    # methods for adding and updating products
    def add_product(self, product):
        self.products.append(product)

    def update_product(self, updated_product):
        for i in range(len(self.products)):
            if self.products[i] == updated_product:
                self.products[i] = updated_product
                break

    # methods for managing stock level
    def update_stock_level(self, product, stock_level):
        for i in range(len(self.products)):
            if self.products[i] == product:
                self.products[i].set_stock_level(stock_level)
                break

    # methods for managing orders
    def add_order(self, order):
        self.orders.append(order)

    def update_order(self, updated_order):
        for i in range(len(self.orders)):
            if self.orders[i] == updated_order:
                self.orders[i] = updated_order
                break

    # methods for managing customer data
    def add_customer(self, customer):
        self.customers.append(customer)

    def update_customer(self, updated_customer):
        for i in range(len(self.customers)):
            if self.customers[i] == updated_customer:
                self.customers[i] = updated_customer
                break