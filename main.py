import turtle
import time
from checkers.game import Game

from draw_board import ChessBoard
from Random.random_agent import random_player
from Minimax import agent, agent_prune

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
            #evaluate time of minimax
            start = time.time()
            # evaluation, move = agent_prune.minimax_prune(game,5, float('-inf'), float('inf'), True, 2)
            evaluation, move = agent.minimax(game,5, True, 2)
            end = time.time()
            print("start::", start, " - end::", end)
            #time is in seconds
            print("Time of minimax::", end-start)
            print("move from minimax::", move)
        game.move(move)
        chess_board.drawPieces(game.board.pieces)
        wn.update()
        time.sleep(1)
    print(game.get_winner())

if __name__ == "__main__":
    main()