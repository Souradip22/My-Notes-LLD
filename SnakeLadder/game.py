from models.board import Board
from models.player import Player




class Game:
    def __init__(self, board_size, player_names, snakes, ladders):
        self.players = [Player(name) for name in player_names]
        self.board = Board(board_size)
        self.board.snake_positions = Game.flatten(snakes)
        self.board.ladder_positions = Game.flatten(ladders)

    @staticmethod
    def flatten(arr):

        op = []
        for pair in arr:
            for e in pair:
                op.append(e)
        return op
    
    def play(self):

        while True:

            for player in self.players:
                roll = player.roll_dice()
                print(player.name + ' Player roll: ' + str(roll))
                self.board.move_player(player, roll)
                print(player.name + " is now on square " + str(player.position))
                if self.board.check_winner(player):
                    return 
                


