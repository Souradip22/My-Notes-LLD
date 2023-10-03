from models.piece import Piece
from models.spot import Spot


class Queen(Piece):
    def __init__(self, white:bool= False):
        super().__init__('Q', white)

    def can_move(self, board, start :Spot, end: Spot):
        if end.get_piece() and end.get_piece().get_white() == self.get_white():
            return False  # Cannot move to a spot occupied by a piece of the same color
        x1 = start.get_x()
        x2 = end.get_x()
        y1 = start.get_y()
        y2 = end.get_y()

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return dx == dy or x1 == x2 or y1 == y2
        # x_diff = abs(start.get_x() - end.get_x())
        # y_diff = abs(start.get_y() - end.get_y())

        # # Queen moves horizontally, vertically, or diagonally
        # if x_diff == y_diff or start.get_x() == end.get_x() or start.get_y() == end.get_y():
        #     # Check if there are no obstructions in the path
        #     if x_diff == y_diff:
        #         # Diagonal movement
        #         x_direction = 1 if end.get_x() > start.get_x() else -1
        #         y_direction = 1 if end.get_y() > start.get_y() else -1
        #         for i in range(1, x_diff):
        #             if board.get_spot(start.get_x() + i * x_direction, start.get_y() + i * y_direction).get_piece():
        #                 return False  # There is an obstruction, invalid move
        #     elif start.get_x() == end.get_x():
        #         # Vertical movement
        #         y_direction = 1 if end.get_y() > start.get_y() else -1
        #         for i in range(1, y_diff):
        #             if board.get_spot(start.get_x(), start.get_y() + i * y_direction).get_piece():
        #                 return False  # There is an obstruction, invalid move
        #     else:
        #         # Horizontal movement
        #         x_direction = 1 if end.get_x() > start.get_x() else -1
        #         for i in range(1, x_diff):
        #             if board.get_spot(start.get_x() + i * x_direction, start.get_y()).get_piece():
        #                 return False  # There is an obstruction, invalid move

        #     return True  # Valid queen move

        # return False  # Invalid move if not moving horizontally, vertically, or diagonally

