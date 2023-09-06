from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from model.Car import Car
from model.Command import Command
from service.ParkingLotService import ParkingLotService
from validator.IntegerValidator import IntegerValidator


class LeaveCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "leave"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(LeaveCommandExecutor, self).__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command):
        params = command.getParams
        if len(params) != 1:
            return False
        return IntegerValidator.isInteger(params[0])

    def execute(self, command: Command):
        slotNum = int(command.getParams[0])
        self.parkingLotService.makeSlotFree(slotNum)
        self.outputPrinter.printStatement(f'Slot number {slotNum} is free')