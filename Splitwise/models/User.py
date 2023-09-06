class User:
    def __init__(self, id: str, name: str, email: str, phone: str):
        self.name = name
        self.id = id
        self.email = email
        self.phone = phone

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getPhone(self):
        return self.phone

    def setPhone(self, phone):
        self.phone = phone


