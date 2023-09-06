from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class StatusCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "status"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(StatusCommandExecutor, self).__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command):
        params = command.getParams
        return len(params) == 0

    def execute(self, command: Command):
        occupiedSlots = self.parkingLotService.getOccupiedSlots()
        if len(occupiedSlots) == 0:
            self.outputPrinter.parkingLotEmpty()
            return
        self.outputPrinter.statusHeader()
        for slot in occupiedSlots:
            parkedCar = slot.getParkedCar()
            slotNumber = slot.getSlotNumber()
            self.outputPrinter.printStatement(f'      {slotNumber}    {parkedCar.getRegistrationNumber()}   {parkedCar.getColor()}')
