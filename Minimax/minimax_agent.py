import random
from checkers.game import Game
import time

def minimax(board, depth, max_player, game):
    if depth == 0 or board.get_winner() != None:
        return None, None
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in board.get_possible_moves():

            evaluation = minimax(board.move(move), depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in board.get_possible_moves():
            evaluation = minimax(board.move(move), depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move

def main():
    game = Game()
    counter = 0
    for piece in game.board.pieces:
        print("player", piece.player)
        print("position piece::", piece.position)
        counter += 1
    print("counter", counter)
    while not game.is_over():
        print(game.board)
        if game.whose_turn() == 1:
            print("Player 1")
            move = minimax(game, 2, game.whose_turn, game)
        else:
            print("Player 2")
            move = random_player(game.board)
        game.move(move)
        time.sleep(1)
    print(game.get_winner())

if __name__ == "__main__":
    main()