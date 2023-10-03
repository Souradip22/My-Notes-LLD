
from models.each_pieces.bishop import Bishop
from models.each_pieces.king import King
from models.each_pieces.night import Night
from models.each_pieces.pawn import Pawn
from models.each_pieces.queen import Queen
from models.each_pieces.rook import Rook
from models.spot import Spot


class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        # Initialize the board with pieces and players
        self.reset_board()



    def reset_board(self):

        # initialize Black pieces
        self.board[0][0] = Spot(Rook(), 0 , 0)
        self.board[0][1] = Spot(Night(), 0 , 1)
        self.board[0][2] = Spot(Bishop(), 0 , 2)
        self.board[0][3] = Spot(Queen(), 0 , 3)
        self.board[0][4] = Spot(King(), 0 , 4)
        self.board[0][5] = Spot(Bishop(), 0 , 5)
        self.board[0][6] = Spot(Night(), 0 , 6)
        self.board[0][7] = Spot(Rook(), 0 , 7)

        self.board[1][0] = Spot(Pawn(), 1 , 0)
        self.board[1][1] = Spot(Pawn(), 1 , 1)
        self.board[1][2] = Spot(Pawn(), 1 , 2)
        self.board[1][3] = Spot(Pawn(), 1 , 3)
        self.board[1][4] = Spot(Pawn(), 1 , 4)
        self.board[1][5] = Spot(Pawn(), 1 , 5)
        self.board[1][6] = Spot(Pawn(), 1 , 6)
        self.board[1][7] = Spot(Pawn(), 1 , 7)

         # initialize White pieces
        self.board[7][0] = Spot(Rook(True), 7, 0)
        self.board[7][1] = Spot(Night(True),7 , 1)
        self.board[7][2] = Spot(Bishop(True), 7, 2)
        self.board[7][3] = Spot(Queen(True), 7 , 3)
        self.board[7][4] = Spot(King(True), 7, 4)
        self.board[7][5] = Spot(Bishop(True),7 , 5)
        self.board[7][6] = Spot(Night(True),7 , 6)
        self.board[7][7] = Spot(Rook(True), 7, 7)

        self.board[6][0] = Spot(Pawn(True), 6 , 0)
        self.board[6][1] = Spot(Pawn(True), 6 , 1)
        self.board[6][2] = Spot(Pawn(True), 6 , 2)
        self.board[6][3] = Spot(Pawn(True), 6 , 3)
        self.board[6][4] = Spot(Pawn(True), 6 , 4)
        self.board[6][5] = Spot(Pawn(True), 6 , 5)
        self.board[6][6] = Spot(Pawn(True), 6 , 6)
        self.board[6][7] = Spot(Pawn(True), 6 , 7)

        for i in range(2, 6):
            for j in range(0, 8):
                self.board[i][j] = Spot(None, i, j)

    def get_board(self):
        return self.board
    
    def get_spot(self, i, j):
        return self.board[i][j]





