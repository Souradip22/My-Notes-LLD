import random

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def roll_dice(self):
        return random.randint(1, 6)
