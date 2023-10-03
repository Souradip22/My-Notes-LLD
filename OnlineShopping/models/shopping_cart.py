class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        for p in self.products:
            if p == product:
                self.products.remove(p)
                break

    def total_cost(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total