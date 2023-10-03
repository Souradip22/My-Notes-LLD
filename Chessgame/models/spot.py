


class Spot:
    def __init__(self, piece, x: int, y: int):
        self.piece = piece
        self.x = x
        self.y = y

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece

    def get_x(self):
        return self.x

    def set_x(self, value):
        self.x = value

    def get_y(self):
        return self.y

    def set_y(self, value):
        self.y = value

    