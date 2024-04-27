import random

def random_player(board):
  move = random.choice(board.get_possible_moves())
  print("Random move: ", move)
  return move
