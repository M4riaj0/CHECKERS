import random
from checkers.game import Game
from copy import deepcopy #Whith this we can copy the game object
import time
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from evaluate_board import eval

# Position is the current position that we are in, is a board object
# depht is the number of moves that we are going to look ahead
# max_player is a boolean that is true if we are the maximizing player and false if we are the minimizing player
def minimax(position, game, depth, max_player, player):
    player2 = 2 if player == 1 else 1
    if depth == 0 or position.get_winner() != None:
        return eval(position.board,player, player2), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in position.board.get_possible_moves():

            evaluation = minimax(position.move(move), game, depth-1, False, player2)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in position.get_possible_moves():
            evaluation = minimax(position.move(move), game, depth-1, True, player2)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move

def main():
    game = Game()
    counter = 0
    # for piece in game.board.pieces:
    #     print("player", piece.player)
    #     print("position piece::", piece.position)
    #     counter += 1
    # print("counter", counter)
    while not game.is_over():
        print(game.board)
        if game.whose_turn() == 1:
            print("Player 1")
            move = minimax(game, game, 2, True, 1)
        # else:
        #     print("Player 2")
        #     move = random_player(game.board)
        game.move(move)
        time.sleep(1)
    print(game.get_winner())

if __name__ == "__main__":
    main()