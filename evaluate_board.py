import random
from checkers.game import Game
import time

# Later we can add the kings to our evaluation function
def eval(board, player1, player2):
    pieces_player1 = len(board.get_pieces_by_player(player1))
    pieces_player2 = len(board.get_pieces_by_player(player2))
    return pieces_player1 - pieces_player2