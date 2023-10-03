from controllers.game_controller import GameController
from models.board import Board
from models.player import HumanPlayer
from services.game_service import GameService



class Color:
    WHITE = "WHITE"
    BLACK = "BLACK"

if __name__ == "__main__":
    white_player = HumanPlayer(True, "Alice")
    black_player = HumanPlayer(False, "Bob")

    chess_game = GameService(white_player, black_player)
    board = chess_game.get_board()
    print(chess_game.get_current_player().name)  # Output: White Player

    # game = Game(white, black)
    controller = GameController(chess_game)
    # GameView.display_game(game)
  
    try:
        
#    0  1  2  3  4  5  6  7
#  +-------------------------
# 0| RB NB BB QB KB BB NB RB |
# 1| PB PB PB -- PB PB PB PB |
# 2| -- -- -- -- -- -- -- -- |
# 3| -- -- -- PB -- -- -- -- |
# 4| -- PH -- -- -- -- -- -- |
# 5| -- -- -- -- -- -- -- -- |
# 6| PH -- PH PH PH PH PH PH |
# 7| RH NH BH QH KH BH NH RH |
#  +--------------------------
#    0  1  2  3  4  5  6  7

        controller.make_move(board.get_spot(6, 1), board.get_spot(5, 1))
        chess_game.print_board()

        
        controller.make_move(board.get_spot(1, 3), board.get_spot(2, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(5, 1), board.get_spot(4, 1))
        chess_game.print_board()

        controller.make_move(board.get_spot(2, 3), board.get_spot(3, 3))
        chess_game.print_board()

        # controller.make_move(board.get_spot(4, 1), board.get_spot(3, 1))
        # chess_game.print_board()

        controller.make_move(board.get_spot(7, 2), board.get_spot(5, 0))
        chess_game.print_board()

        controller.make_move(board.get_spot(3, 3), board.get_spot(4, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(5, 0), board.get_spot(1, 4))
        chess_game.print_board()


        controller.make_move(board.get_spot(4, 3), board.get_spot(5, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(6, 3), board.get_spot(5, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(0, 4), board.get_spot(1, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(5, 3), board.get_spot(4, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(1, 3), board.get_spot(2, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(4, 3), board.get_spot(3, 3))
        chess_game.print_board()

        controller.make_move(board.get_spot(1, 0), board.get_spot(2, 0))
        chess_game.print_board()

        controller.make_move(board.get_spot(3, 3), board.get_spot(2, 3))
        chess_game.print_board()



        


        



        # controller.make_move(board.get_spot(4, 1), board.get_spot(3, 1))
        # chess_game.print_board()


        # controller.make_move(board.get_spot(3, 3), board.get_spot(4, 3))
        # chess_game.print_board()

        # controller.make_move(board.get_spot(3, 1), board.get_spot(2, 1))
        # chess_game.print_board()


        # controller.make_move(board.get_spot(4, 3), board.get_spot(5, 3))
        # chess_game.print_board()

        # controller.make_move(board.get_spot(2, 1), board.get_spot(1, 1))
        # chess_game.print_board()


        # controller.make_move(board.get_spot(5, 3), board.get_spot(6, 3))
        # chess_game.print_board()
        # controller.make_move(board.get_box(1, 3), board.get_box(3, 3))
        # GameView.display_game(game)
        # controller.make_move(board.get_box(7, 5), board.get_box(5, 4))
        # GameView.display_game(game)
        # ... continue making moves as needed
    except Exception as e:
        print("Error:", str(e))
