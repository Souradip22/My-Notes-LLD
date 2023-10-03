class RoomBooking:
    def __init__(self, room, guest_name, number_of_nights):
        self.room = room
        self.guest_name = guest_name
        self.number_of_nights = number_of_nights

    def get_room(self):
        return self.room

    def get_guest_name(self):
        return self.guest_name

    def get_number_of_nights(self):
        return self.number_of_nights