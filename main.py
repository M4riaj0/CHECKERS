import turtle
import time
from checkers.game import Game

from draw_board import ChessBoard
from Random.random_agent import random_player
from Minimax import minimax_agent, minimax_agent_prune

def main():
    game = Game()
    counter = 0
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
            evaluation, move = minimax_agent.minimax(game,3, True, 2)
            print("move from minimax::", move)
        game.move(move)
        chess_board.drawPieces(game.board.pieces)
        wn.update()
        time.sleep(1)
    print(game.get_winner())

if __name__ == "__main__":
    main()