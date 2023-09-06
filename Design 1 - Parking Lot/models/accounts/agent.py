from interfaces.i_account import Account


class ParkingAgen(Account):
    def __init__(self, user_name, password, person, status) -> None:
        super().__init__(user_name, password, person, status)

    
    def process_ticket(self, ticker_number):
        pass

    def reset_password(self):
        return super().reset_password()