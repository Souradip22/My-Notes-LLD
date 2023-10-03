from models.piece import Piece
from models.spot import Spot
import math



class King(Piece):
    def __init__(self, white:bool= False):
        super().__init__('K', white)
        self.is_castling_done = False




    def can_move(self, board, start :Spot, end: Spot):
        print('here==')
        if end.get_piece() and end.get_piece().get_white() == self.get_white():
            return False
        x1 = start.get_x()
        x2 = end.get_x()
        y1 = start.get_y()
        y2 = end.get_y()
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return dx <= 1 and dy <= 1
        
        # x_diff = abs(start.get_x() - end.get_x())
        # y_diff = abs(start.get_y() - end.get_y())

        # # King moves one square in any direction
        # if x_diff + y_diff == 1:
        #     return True

        # # King can also make a valid move if it's a diagonal move (x_diff == y_diff) of length sqrt(2)
        # if x_diff == 1 and y_diff == 1:
        #     return True

        # return False
            
            
    def is_valid_castling(self, board, start :Spot, end: Spot):
         
         if self.get_is_castling_done():
              return False
            
    
    def get_is_castling_done(self):
        return self.is_castling_done

    def set_is_castling_done(self, value):
        self.is_castling_done = value
