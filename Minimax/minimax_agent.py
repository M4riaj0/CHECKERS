import random
from checkers.game import Game
from copy import deepcopy #Whith this we can copy the game object
import time
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from evaluate_board import evaluate_board

# Position is the current position that we are in, is a board object
# depht is the number of moves that we are going to look ahead
# max_player is a boolean that is true if we are the maximizing player and false if we are the minimizing player
def minimax(position, game, depth, max_player, player):
    if depth == 0 or position.get_winner() != None:
        player2 = 2 if player == 1 else 1
        return evaluate_board(position,player, player2), position
    
    if max_player:
        max_eval = float('-inf')
    else:
        pass