from controllers.game_controller import GameController
from models.board import Board
# from models.piece import Piece

class GameService:
    def __init__(self, white, black):
        self.current_player = white
        self.board = Board()
        self.moves = []
        self.game_result = ""
        self.white = white
        self.black = black

    def get_current_player(self):
        return self.current_player

    def switch_current_player(self):
        self.current_player = self.black if self.current_player == self.white else self.white

    def get_board(self):
        return self.board

    def get_moves(self):
        return self.moves

    def add_move(self, move):
        self.moves.append(move)

    def remove_last_move(self):
        if self.moves:
            self.moves.pop()

    def set_game_result(self, result):
        self.game_result = result

    def get_game_result(self):
        return self.game_result
    
    def print_board(self):
        board = self.board.get_board()
        print("   0  1  2  3  4  5  6  7 ")
        print(" +-------------------------")
        for row in range(8):
            print(f"{row}|", end=" ")
            for col in range(8):
                spot = board[row][col]
                if spot is None:
                    print(".", end = "")
                else:
                    if spot.get_piece() and spot.get_piece().get_symbol():
                        name = spot.get_piece().get_symbol()
                        if spot.get_piece().get_white() == True:
                            name = name + 'H'
                        else:
                            name = name + 'B'

                        print(name, end=" ")
                    else:
                        print('--', end= " ")
                # if piece is None:
                #     print(".", end=" ")
                # else:
                #     print(piece.get_symbol() + piece.get_white(), end=" ")
            print("|")
        print(" +--------------------------")
        print("   0  1  2  3  4  5  6  7 ")

    # def make_move(self, start, end):
    #     current_player = self.players[self.current_player]
    #     self.chess_controller.move_piece(start, end, current_player)
    #     self.print_board()
    #     self.current_player = 1 - self.current_player  # Switch player turn

