from OutputPrinter import OutputPrinter
from commands.CreateParkingLotCommandExecutor import CreateParkingLotCommandExecutor
from commands.ParkCommandExecutor import ParkCommandExecutor
from commands.LeaveCommandExecutor import LeaveCommandExecutor
from commands.StatusCommandExecutor import StatusCommandExecutor
from commands.ColorToRegNumberCommandExecutor import ColorToRegNumberCommandExecutor
from commands.ColorToSlotNumberCommandExecutor import  ColorToSlotNumberCommandExecutor
from commands.SlotForRegNumberCommandExecutor import SlotForRegNumberCommandExecutor
from commands.ExitCommandExecutor import ExitCommandExecutor
from exception.InvalidCommandException import InvalidCommandException
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class CommandExecutorFactory:

    commands = {}

    def __init__(self, parkingLotService: ParkingLotService):
        outputPrinter = OutputPrinter()
        self.__class__.commands[CreateParkingLotCommandExecutor.COMMAND_NAME] = CreateParkingLotCommandExecutor(parkingLotService, outputPrinter)
        self.__class__.commands[ParkCommandExecutor.COMMAND_NAME] = ParkCommandExecutor(parkingLotService, outputPrinter)
        self.__class__.commands[LeaveCommandExecutor.COMMAND_NAME] = LeaveCommandExecutor(parkingLotService, outputPrinter)
        self.__class__.commands[StatusCommandExecutor.COMMAND_NAME] = StatusCommandExecutor(parkingLotService, outputPrinter)
        self.__class__.commands[ColorToRegNumberCommandExecutor.COMMAND_NAME] = ColorToRegNumberCommandExecutor(parkingLotService, outputPrinter)
        self.__class__.commands[ColorToSlotNumberCommandExecutor.COMMAND_NAME] = ColorToSlotNumberCommandExecutor(parkingLotService, outputPrinter)
        self.__class__.commands[SlotForRegNumberCommandExecutor.COMMAND_NAME] = SlotForRegNumberCommandExecutor(parkingLotService, outputPrinter)
        self.__class__.commands[ExitCommandExecutor.COMMAND_NAME] = ExitCommandExecutor(parkingLotService, outputPrinter)

    @staticmethod
    def getCommandExecutor(command: Command):
        commandExecutor = CommandExecutorFactory.commands.get(command.getCommandName)
        if commandExecutor is None:
            raise InvalidCommandException()
        return commandExecutor;

