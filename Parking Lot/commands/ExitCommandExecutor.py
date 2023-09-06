from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class ExitCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "exit"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(ExitCommandExecutor, self).__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command):
        params = command.getParams
        return len(params) == 0

    def execute(self, command: Command):
        self.outputPrinter.end()