class ExpenseMetaData:
    def __init__(self, name: str, imageUrl: str, notes: str):
        self.name = name
        self.imageUrl = imageUrl
        self.notes = notes

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getImageUrl(self):
        return self.imageUrl

    def setImageUrl(self, imageUrl):
        self.imageUrl = imageUrl

    def getNotes(self):
        return self.notes

    def setNotes(self, notes):
        self.notes = notes
