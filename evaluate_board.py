import random
from checkers.game import Game
import time

# Later we can add the kings to our evaluation function
def eval(board, player1, player2):
    pieces_player1 = len(board.searcher.get_pieces_by_player(player1))
    pieces_player2 = len(board.searcher.get_pieces_by_player(player2))
    kings_player2 = 0
    kings_player1 = 0
    #add kings to the evaluation
    for piece in board.pieces:
        if piece.king:
            if piece.player == player1:
                kings_player1 += 1
            else:
                kings_player2 += 1
    return (pieces_player1 + kings_player1) - (pieces_player2 + kings_player2)