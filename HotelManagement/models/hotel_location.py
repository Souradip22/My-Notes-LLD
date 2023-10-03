class HotelLocation:
    def __init__(self, location, address, phone_number):
        self.location = location
        self.address = address
        self.phone_number = phone_number

    def get_location(self):
        return self.location

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number