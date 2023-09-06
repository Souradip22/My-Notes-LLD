import abc

from OutputPrinter import OutputPrinter
from commands.CommandExecutorFactory import CommandExecutorFactory
from exception.InvalidCommandException import InvalidCommandException


class Mode(metaclass=abc.ABCMeta):

    def __init__(self, commandExecutorFactory: CommandExecutorFactory, outputPrinter: OutputPrinter):
        self.outputPrinter = outputPrinter
        self.commandExecutorFactory = commandExecutorFactory

    # Helper method to process a command. it basically uses [CommandExecutor] to run the given command

    def processCommand(self, command):
        commandExecutor = self.commandExecutorFactory.getCommandExecutor(command)
        if commandExecutor.validate(command):
            commandExecutor.execute(command)
        else:
            raise InvalidCommandException()

    # Helper method to process the mode. Each mode will process in its own way
    @abc.abstractmethod
    def process(self):
        pass
