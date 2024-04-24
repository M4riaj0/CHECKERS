import random
from checkers.game import Game
import time

# Review the pieces on the board:

# for piece in game.board.pieces:
# 	piece.player #1 or 2
# 	piece.other_player #1 or 2
# 	piece.king #True or False
# 	piece.captured #True or False
# 	piece.position #1-32
# 	piece.get_possible_capture_moves() #[[int, int], [int, int], ...]
# 	piece.get_possible_positional_moves() #[[int, int], [int, int], ...]

# ------------------- This will be changed to another file -------------------

# ------------------- This will be changed to another file -------------------


def random_player(board, counter=0):
  move = random.choice(board.get_possible_moves())
  print("Random move: ", move)
  return move

def main():
    game = Game()
    counter = 0
    for piece in game.board.pieces:
        print("player", piece.player)
        print("position piece::", piece.position)
        counter += 1
    print("counter", counter)
    # while not game.is_over():
    #     print(game.board)
    #     if game.whose_turn() == 1:
    #      print("Player 1")
    #      move = random_player(game.board)
    #     else:
    #         print("Player 2")
    #         move = random_player(game.board)
    #     game.move(move)
    #     time.sleep(1)
    # print(game.get_winner())

if __name__ == "__main__":
    main()