from interfaces.i_account import Account


class Admin(Account):
    def __init__(self, user_name, password, person, status) -> None:
        super().__init__(user_name, password, person, status)

    def add_parking_spot(self, spot): # here spot = ParkingSpot class reference
        pass

    def add_display_board(self, display_board): # here display_board = DisplayBoard class ref

        pass

    def add_entrance(self, entracne):# entrance = Enterance Class refs

        pass

    def add_exit(self, exit):
        pass

    def reset_password(self):
        return super().reset_password()


