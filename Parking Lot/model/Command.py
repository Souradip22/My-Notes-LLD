from exception.InvalidCommandException import InvalidCommandException


class Command:
    params: list[str]
    commandName: str
    SPACE = " ",

    def __init__(self, inputLine: str):
        tokensList = list(inputLine.strip().split())
        print('Current Command --> ', tokensList)
        if len(tokensList) == 0:
            raise InvalidCommandException()

        self.commandName = tokensList[0]
        self.params = tokensList[1:]

    @property
    def getCommandName(self):
        return self.commandName

    @property
    def getParams(self):
        return self.params





