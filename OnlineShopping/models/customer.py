class Customer:
    def __init__(self, name="", address="", email=""):
        self.name = name
        self.address = address
        self.email = email

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_email(self, email):
        self.email = email

    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.name == other.name and self.address == other.address and self.email == other.email
        return False