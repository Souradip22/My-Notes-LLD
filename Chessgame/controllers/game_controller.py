
from models.move import Move


class GameController:
    def __init__(self, game):
        self.game = game

    def make_move(self, from_spot, to_spot):
        if from_spot is None or to_spot is None:
            raise ValueError("Invalid move.")

        piece = from_spot.get_piece()
        piece.get_piece_info()
        if piece is None or piece.get_white() != self.game.get_current_player().is_white_side():
            print('eher')
            raise ValueError("Invalid Player Turn")
        
        if not piece.can_move(self.game.get_board(), from_spot, to_spot):
            print('eher==')
            raise ValueError("Invalid move for " + str(piece.get_symbol()))
        move = Move(self.game.get_current_player(), from_spot, to_spot)
        if to_spot.get_piece() is None:
            move.set_piece(to_spot.get_piece())
        else:
            move.set_piece(to_spot.get_piece())

        
        self.game.add_move(move)
        # piece.set_killed(True)
        if (from_spot.get_piece() and to_spot.get_piece()):
            print("stay")
            to_spot.get_piece().set_killed(True)

        if to_spot.get_piece() and to_spot.get_piece().get_symbol() == 'K' and to_spot.get_piece().get_killed():
            print(str(self.game.get_current_player().name) + " has WON!!")
            
            # return str(self.game.get_current_player().name) + " has WON!!"
            # raise ValueError(str(self.game.get_current_player().name) + " has WON!!")
        to_spot.set_piece(piece)

        from_spot.set_piece(None)
        self.game.switch_current_player()

        