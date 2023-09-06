class ParkingLotException(RuntimeError):
    def __init__(self, message=''):
        super(ParkingLotException, self).__init__(message)
