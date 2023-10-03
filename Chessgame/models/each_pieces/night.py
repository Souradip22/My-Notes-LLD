from models.piece import Piece
from models.spot import Spot
import math


class Night(Piece):
    def __init__(self, white:bool = False):
        super().__init__('N', white)

    def can_move(self, board, start :Spot, end: Spot):
            
        if end.get_piece() and end.get_piece().get_white() == self.get_white():
            return False
        

        x1 = start.get_x()
        x2 = end.get_x()
        y1 = start.get_y()
        y2 = end.get_y()

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)
        
        # x_diff = abs(start.get_x() - end.get_x())
        # y_diff = abs(start.get_y() - end.get_y())

        # # Knight moves in L-shape: 2 squares in one direction and 1 square perpendicular to that
        # return (x_diff == 2 and y_diff == 1) or (x_diff == 1 and y_diff == 2)
