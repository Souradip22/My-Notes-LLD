class Board:
    def __init__(self, size):
        self.size = size
        self.player_positions = []
        self.snake_positions = []
        self.ladder_positions = []

    def move_player(self, player, roll):
        if player.position + roll > self.size:
            print('Invalid roll')
            return
        
        newPosition = player.position + roll

        for i in range(0, len(self.snake_positions), 2):
            if newPosition == self.snake_positions[i]:
                newPosition = self.snake_positions[ i + 1]
                break

        for i in range(0, len(self.ladder_positions), 2):
            if newPosition == self.ladder_positions[i]:
                newPosition = self.ladder_positions[ i + 1]
                break

        player.position = newPosition

        



    def check_winner(self, player):
        if player.position == self.size:
            print('Player ' + player.name + ' has won')
            return True
        return False
