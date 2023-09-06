from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class ColorToRegNumberCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "registration_numbers_for_cars_with_colour"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(ColorToRegNumberCommandExecutor, self).__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command):
        params = command.getParams
        return len(params) == 1

    def execute(self, command: Command):
        slotsForColor = self.parkingLotService.getSlotsForColor(command.getParams[0]);
        if len(slotsForColor) == 0:
            self.outputPrinter.notFound()
            return

        for slot in slotsForColor:
            parkedCar = slot.getParkedCar()
            slotNumber = slot.getSlotNumber()
            self.outputPrinter.printStatement(f'Registration Number {parkedCar.getRegistrationNumber()} with color {parkedCar.getColor()}')