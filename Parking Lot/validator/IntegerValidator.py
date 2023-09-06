class IntegerValidator:
    @staticmethod
    def isInteger(inp: str):
        try:
            i = int(inp)
            return True
        except ValueError as verr:
            print("FROM INTEGER VALIDATOR")
            return False
