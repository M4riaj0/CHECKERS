import turtle
import time
from checkers.game import Game

from draw_board import ChessBoard, person_play
from Random.random_agent import random_player
from Minimax import agent, agent_prune
from Qlearning.q_agent import QlearningAgent

def main():
    game = Game()
    counter = 0
    wn = turtle.Screen()
    wn.tracer(0, 0)
    wn.title("Checkers Game")
    q_agent = QlearningAgent(0.5, 0.1, 0.9, lambda board: board.get_possible_moves())

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
        state = game.board.searcher.player_positions
        print("state::", state)
        if game.whose_turn() == 1:
         print("Player 1")
         move = person_play(game, chess_board, wn)
        #  state = game.board.searcher.player_positions
        #  state = tuple(tuple(vals) for vals in state.values())
        #  move = q_agent.get_action(game.board, state)
        #  move = list(move)
        #  move = random_player(game.board)
        else:
            print("Player 2")
            #evaluate time of minimax
            start = time.time()
            # move = random_player(game.board)
            # evaluation, move = agent_prune.minimax_prune(game,5, float('-inf'), float('inf'), True, 2)
            # evaluation, move = agent.minimax(game,3, True, 2)
            move = random_player(game.board)
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