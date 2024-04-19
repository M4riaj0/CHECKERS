import random
from checkers.game import Game
import time

def random_player(board):
  move = random.choice(board.get_possible_moves())
  return move

def main():
    game = Game()
    while not game.is_over():
        print(game.board)
        print(game.get_winner())
        if game.whose_turn == 1:
         move = random_player(game.board)
        else:
            move = random_player(game.board)
        game.move(move)
        time.sleep(1)
    print(game.get_winner())

if __name__ == "__main__":
    main()