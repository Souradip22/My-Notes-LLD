from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from model.Command import Command
from model.ParkingLot import ParkingLot
from model.ParkingStrategy.NaturalOrderParkingStrategy import NaturalOrderParkingStrategy
from service.ParkingLotService import ParkingLotService
from validator.IntegerValidator import IntegerValidator


class CreateParkingLotCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "create_parking_lot"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(CreateParkingLotCommandExecutor, self).__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command):
        params = command.getParams
        if len(params) != 1:
            return False

        return IntegerValidator.isInteger(params[0])

    def execute(self, command: Command):
        parkingLotCapacity = int(command.getParams[0])
        parkingLot: ParkingLot = ParkingLot(parkingLotCapacity)
        parkingStrategy: NaturalOrderParkingStrategy = NaturalOrderParkingStrategy()
        self.parkingLotService.createParkingLot(parkingLot, parkingStrategy)
        self.outputPrinter.printStatement(f'Created a parking lot with {parkingLot.getCapacity()} slots')

