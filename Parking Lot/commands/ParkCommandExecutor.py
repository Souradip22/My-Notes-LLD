from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from exception.NoFreeSlotAvailableException import NoFreeSlotAvailableException
from model.Car import Car
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class ParkCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "park"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(ParkCommandExecutor, self).__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command):
        params = command.getParams
        return len(params) == 2

    def execute(self, command: Command):
        car: Car = Car(command.getParams[0], command.getParams[1])
        try:
            slot = self.parkingLotService.park(car)
            self.outputPrinter.printStatement(f'Allocated slot number {slot}')
        except NoFreeSlotAvailableException:
            self.outputPrinter.parkingLotFull()

        # parkingLotCapacity = int(command.getParams[0])
        # print('parkingLotCapacity', parkingLotCapacity)
        # parkingLot: ParkingLot = ParkingLot(parkingLotCapacity)
        # parkingStrategy: NaturalOrderParkingStrategy = NaturalOrderParkingStrategy()
        # self.parkingLotService.createParkingLot(parkingLot, parkingStrategy)
        # self.outputPrinter.printStatement(f'Created a parking lot with {parkingLot.getCapacity()} slots')
