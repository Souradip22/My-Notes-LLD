from abc import ABC, abstractmethod

from models.spot import Spot


class Piece(ABC):
    def __init__(self, symbol:str, white:bool, killed:bool = None):
        self.white = white
        self.killed = killed
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, value):
        self.symbol = value


    def get_white(self):
        return self.white

    def set_white(self, value):
        self.white = value

    def get_killed(self):
        return self.killed

    def set_killed(self, value):
        self.killed = value

    def get_piece_info(self):

        print(self.symbol , self.white)
        return


    @abstractmethod
    def can_move(self, board, start :Spot, end: Spot):
        pass
    


