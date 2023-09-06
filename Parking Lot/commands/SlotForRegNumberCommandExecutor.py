from OutputPrinter import OutputPrinter
from commands.CommandExecutorInterface import CommandExecutorInterface
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class SlotForRegNumberCommandExecutor(CommandExecutorInterface):
    COMMAND_NAME = "slot_number_for_registration_number"

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.parkingLotService = parkingLotService
        self.outputPrinter = outputPrinter
        super(SlotForRegNumberCommandExecutor, self).__init__(parkingLotService, outputPrinter)

    def validate(self, command: Command):
        params = command.getParams
        return len(params) == 1

    def execute(self, command: Command):
        occupiedSlots = self.parkingLotService.getOccupiedSlots()
        regNumber = command.getParams[0]
        if len(occupiedSlots) == 0:
            self.outputPrinter.notFound()
            return

        for slot in occupiedSlots:

            parkedCar = slot.getParkedCar()
            if parkedCar.getRegistrationNumber() == regNumber:
                slotNumber = slot.getSlotNumber()
                return self.outputPrinter.printStatement(
                    f'Slot Number {slotNumber} with Reg Number {regNumber}')
        return  self.outputPrinter.notFound()
