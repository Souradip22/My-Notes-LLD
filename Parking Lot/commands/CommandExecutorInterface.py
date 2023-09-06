import abc

from OutputPrinter import OutputPrinter
from model.Command import Command
from service.ParkingLotService import ParkingLotService


class CommandExecutorInterface(metaclass=abc.ABCMeta):

    def __init__(self, parkingLotService: ParkingLotService, outputPrinter: OutputPrinter):
        self.outputPrinter = outputPrinter
        self.parkingLotService = parkingLotService

    @abc.abstractmethod
    def validate(self, command: Command):
        pass

    @abc.abstractmethod
    def execute(self, command: Command):
        pass
