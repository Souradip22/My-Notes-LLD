from models.piece import Piece
from models.spot import Spot


class Pawn(Piece):
    def __init__(self, white:bool= False):
        super().__init__('P',white)

    def can_move(self, board, start :Spot, end: Spot):
        if end.get_piece() and end.get_piece().get_white() == self.get_white():
            return False  # Cannot move to a spot occupied by a piece of the same color
        x1 = start.get_x()
        x2 = end.get_x()
        y1 = start.get_y()
        y2 = end.get_y()

    # Pawns can only move vertically
        if y1 != y2:
            return False

        if self.get_white():
            # White pawns can move one square forward or two squares forward on their first move
            if x2 == x1 - 1 or (x1 == 6 and x2 == 4):
                return True
        else:  # Assuming opposite player is black
            # Black pawns can move one square forward or two squares forward on their first move
            if x2 == x1 + 1 or (x1 == 1 and x2 == 3):
                return True
        
        return False

        # # For white pawns, they can move forward (y_diff == 1)
        # # For the first move, they can move forward two squares (y_diff == 2)
        # if self.get_white() and y_diff <= 2 and x_diff == 0 and end.get_piece() is None:
        #     if y_diff == 2 and start.get_y() != 1:
        #         return False  # Invalid move for white pawn, not the first move
        #     return True

        # # For black pawns, they can move forward (y_diff == 1)
        # # For the first move, they can move forward two squares (y_diff == 2)
        # if not self.get_white() and y_diff <= 2 and x_diff == 0 and end.get_piece() is None:
        #     if y_diff == 2 and start.get_y() != 6:
        #         return False  # Invalid move for black pawn, not the first move
        #     return True

        # # Pawns can capture diagonally
        # if y_diff == 1 and x_diff == 1 and end.get_piece() is not None:
        #     return True

        # return False  # Invalid move for pawn
