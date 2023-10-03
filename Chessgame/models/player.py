class Player:
    def __init__(self, white_side, human_player):
        self.white_side = white_side
        self.human_player = human_player

    def is_white_side(self):
        return self.white_side

    def is_human_player(self):
        return self.human_player

class HumanPlayer(Player):
    def __init__(self, white_side, name):
        super().__init__(white_side, True)
        self.name = name

class ComputerPlayer(Player):
    def __init__(self, white_side):
        super().__init__(white_side, False)