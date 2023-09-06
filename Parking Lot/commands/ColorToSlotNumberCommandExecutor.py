from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class ColorToSlotNumberCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "slot_numbers_for_cars_with_colour"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(ColorToSlotNumberCommandExecutor, self).__init__(parkingLotService, outputPrinter)

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
            self.outputPrinter.printStatement(f'Slot Number {slotNumber} with color {parkedCar.getColor()}')