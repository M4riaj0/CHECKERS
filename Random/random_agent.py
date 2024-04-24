import random
import turtle
from checkers.game import Game
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from draw_board import ChessBoard
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



def random_player(board, counter=0):
  move = random.choice(board.get_possible_moves())
  print("Random move: ", move)
  return move

def main():
    game = Game()
    counter = 0
    # Configurar la pantalla
    # Configurar la pantalla
    wn = turtle.Screen()
    wn.tracer(0, 0)
    wn.title("Checkers Game")

    # Crear el tablero de ajedrez y las fichas
    chess_board = ChessBoard(wn, game.board.pieces)
    # Mantener la ventana abierta
    wn.update()
    chess_board.drawPieces(game.board.pieces)
    for piece in game.board.pieces:
        print("player", piece.player)
        print("position piece::", piece.position)
        counter += 1
    print("counter", counter)
    while not game.is_over():
        print(game.board)
        if game.whose_turn() == 1:
         print("Player 1")
         move = random_player(game.board)
        else:
            print("Player 2")
            move = random_player(game.board)
        game.move(move)
        chess_board.drawPieces(game.board.pieces)
        wn.update()
        time.sleep(1)
    print(game.get_winner())

if __name__ == "__main__":
    main()