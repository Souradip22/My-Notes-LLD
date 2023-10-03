class RoomHouseKeeping:
    def __init__(self, room, date, status):
        self.room = room
        self.date = date
        self.status = status

    def get_room(self):
        return self.room

    def get_date(self):
        return self.date

    def get_status(self):
        return self.status