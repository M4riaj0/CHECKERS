import random
from checkers.game import Game
from copy import deepcopy #With this we can copy the game object
import time
from evaluate_board import eval

# Position is the current position that we are in, is a board object
# depht is the number of moves that we are going to look ahead
# max_player is a boolean that is true if we are the maximizing player and false if we are the minimizing player
def minimax_prune(position,depth,alpha, beta ,max_player, player):
    if depth == 0 or position.get_winner() != None:
        player2 = 2 if player == 1 else 1
        return eval(position.board,player, player2), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position):
            evaluation  = minimax_prune(move[0], depth-1,alpha, beta, False, player)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move[1]
            alpha = max(alpha, maxEval)
            if beta <= alpha:
              break
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position):
            evaluation = minimax_prune(move[0], depth-1, alpha, beta, True, player)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move[1]
            beta = min(alpha, minEval)
            if beta <= alpha:
              break
        return minEval, best_move
    

def get_all_moves(position):
    moves_played = []
    for move in position.board.get_possible_moves():
        temp_board = deepcopy(position)
        temp_board.move(move)
        moves_played.append([temp_board, move])

    return moves_played
