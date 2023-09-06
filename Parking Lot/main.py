# This is a sample Python script.
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from OutputPrinter import OutputPrinter
from commands.CommandExecutorFactory import CommandExecutorFactory
from exception.InvalidModeException import InvalidModeException
from mode.FileMode import FileMode
from mode.InteractiveMode import InteractiveMode
from service.ParkingLotService import ParkingLotService

fileName = sys.argv[1]

outputPrinter: OutputPrinter = OutputPrinter()
parkingLotService: ParkingLotService = ParkingLotService()
commandExecutorFactory: CommandExecutorFactory = CommandExecutorFactory(parkingLotService)


def isInteractiveMode(args):
    pass


def isFileInputMode(inpFileName: str):
    return inpFileName


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if isFileInputMode(fileName):
        FileMode(commandExecutorFactory, outputPrinter, fileName).process()
    # elif isFileInputMode(param):
    #     InteractiveMode(commandExecutorFactory, outputPrinter).process()
    else:
        raise InvalidModeException();

