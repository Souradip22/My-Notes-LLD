from game import Game


if __name__ == "__main__":
    player_names = ["Alice", "Bob"]
    snakes = [(16, 6), (47, 30), (49, 1), (56, 8)]  # Example snake positions
    ladders = [(2, 38), (7, 14), (8, 31), (15, 26)]  # Example ladder positions
    game = Game(100, player_names, snakes, ladders)
    game.play()