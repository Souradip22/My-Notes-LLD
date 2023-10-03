class Product:
    def __init__(self, name, description, price, stock_level):
        self.name = name
        self.description = description
        self.price = price
        self.stock_level = stock_level

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_stock_level(self):
        return self.stock_level

    def set_name(self, name):
        self.name = name

    def set_description(self, description):
        self.description = description

    def set_price(self, price):
        self.price = price

    def set_stock_level(self, stock_level):
        self.stock_level = stock_level

    def __eq__(self, other):
        return (
            self.get_name() == other.get_name()
            and self.get_description() == other.get_description()
            and self.get_price() == other.get_price()
            and self.get_stock_level() == other.get_stock_level()
        )

    def __hash__(self):
        return hash((self.get_name(), self.get_description(), self.get_price(), self.get_stock_level()))