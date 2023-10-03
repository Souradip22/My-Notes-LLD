class Move:
    def __init__(self, player, start, end):
        self.player = player
        self.start = start
        self.end = end
        self.piece_moved = start.get_piece()
        self.piece_killed = None
        self.castling_move = False

    def is_castling_move(self):
        return self.castling_move

    def set_castling_move(self, castling_move):
        self.castling_move = castling_move

    def set_piece(self, piece):
        self.piece = piece
