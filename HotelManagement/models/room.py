class Room:
    def __init__(self, room_number, room_style, booking_price):
        self.room_number = room_number
        self.room_style = room_style
        self.booking_price = booking_price

    def get_room_number(self):
        return self.room_number

    def get_room_style(self):
        return self.room_style

    def get_booking_price(self):
        return self.booking_price