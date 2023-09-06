from OutputPrinter import OutputPrinter
from commands.CommandExecutorFactory import CommandExecutorFactory
from mode.Mode import Mode
from model.Command import Command


class FileMode(Mode):

    def __init__(self, commandExecutorFactory: CommandExecutorFactory, outputPrinter: OutputPrinter, fileName=None):
        super(FileMode, self).__init__(commandExecutorFactory, outputPrinter)
        self.filename = fileName

    def process(self):
        try:
            with open(self.filename, 'r') as f:
                inputCommand = f.readline()
                while inputCommand != '':
                    command = Command(inputCommand)
                    self.processCommand(command)
                    inputCommand = f.readline()
        except FileNotFoundError as e:
            OutputPrinter.invalidFile()
            print(f"FileNotFoundError successfully handled\n"
                  f"{e}")
            return

