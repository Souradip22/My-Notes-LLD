from models.piece import Piece
from models.spot import Spot


class Bishop(Piece):
    def __init__(self, white:bool= False):
        super().__init__('B',white)

    def can_move(self, board, start :Spot, end: Spot):
        if end.get_piece() and end.get_piece().get_white() == self.get_white():
            return False

        x1 = start.get_x()
        x2 = end.get_x()
        y1 = start.get_y()
        y2 = end.get_y()

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        return dx == dy
        # x_diff = abs(start.get_x() - end.get_x())
        # y_diff = abs(start.get_y() - end.get_y())

        # # Bishop moves diagonally, so x_diff must be equal to y_diff for valid movement
        # if x_diff == y_diff:
        #     # Check if there are no obstructions in the diagonal path
        #     min_x, max_x = min(start.get_x(), end.get_x()), max(start.get_x(), end.get_x())
        #     min_y, max_y = min(start.get_y(), end.get_y()), max(start.get_y(), end.get_y())
        #     for x in range(min_x + 1, max_x):
        #         for y in range(min_y + 1, max_y):
        #             if board.get_spot(x, y).get_piece():
        #                 return False  # There is an obstruction, invalid move

        #     return True  # Valid diagonal move

        # return False  # Invalid move if not moving diagonally or if there are obstructions
