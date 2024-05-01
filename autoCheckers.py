# We would use this file as an implementation for AutoCheckers,
# we find a project rather similar to our assigned homework here: https://hendrix-cs.github.io/csci335/projects/checkers.html they describe it as:

# AutoCheckers: A GUI that can run exprimental tournaments to compare the ability of different AI players.

# AutoCheckers is a program implemented in java, but we are using python, so we will have to adapt the code to our needs.

# the original repository of this code is: https://github.com/gjf2a/csci335 and you can find the file in src/checkers/gui/AutoCheckers.java


import turtle
import time
import statistics
import matplotlib.pyplot as plt
from checkers.game import Game
from Random.random_agent import random_player
from Minimax import agent, agent_prune
from copy import deepcopy #With this we can copy the game object

# Función para ejecutar un juego
def run_game(player1, player2):
    game = Game()
    player1_time = 0
    player2_time = 0
    new_game = deepcopy(game)
    print("winner::", new_game.get_winner())
    while not new_game.is_over():
        if new_game.whose_turn() == 1:
            start_time = time.time()
            move = player1(new_game)
            end_time = time.time()
            player1_time += end_time - start_time
        else:
            start_time = time.time()
            move = player2(new_game)
            end_time = time.time()
            player2_time += end_time - start_time
        new_game.move(move)
    print("winner::", new_game.get_winner())
    return player1_time, player2_time, new_game.get_winner()

# Función para ejecutar múltiples juegos y calcular estadísticas
def run_multiple_games(player1, player2, num_games):
    total_times_player1 = []
    total_times_player2 = []
    winners = []
    print("Running ", num_games, " games...")
    for _ in range(num_games):
        player1_time, player2_time, winner = run_game(player1, player2)
        total_times_player1.append(player1_time)
        total_times_player2.append(player2_time)
        winners.append(winner)
    print("Games finished.")
    avg_time_player1 = statistics.mean(total_times_player1)
    avg_time_player2 = statistics.mean(total_times_player2)
    player1_wins = winners.count(1)
    player2_wins = winners.count(2)
    draws = winners.count(None)
    return avg_time_player1, avg_time_player2, player1_wins, player2_wins, draws

# Función para dibujar una gráfica de barras de los resultados
def draw_bar_chart(player1_wins, player2_wins, draws):
    players = ['Player 1', 'Player 2', 'Draws']
    wins = [player1_wins, player2_wins, draws]
    plt.bar(players, wins)
    plt.xlabel('Players')
    plt.ylabel('Wins')
    plt.title('Game Results')
    plt.show()

# Función principal
def main():
    wn = turtle.Screen()
    wn.title("Checkers Game Interface")
    wn.bgcolor("white")

    # Configuración de la interfaz
    num_games = int(wn.numinput("Number of games", "Enter the number of games to play:", default=10))

     # Funciones de los jugadores
    def random_agent(board):
        return random_player(board)

    def minimax_agent(board):
        _, move = agent.minimax(board, 5, True, 2)
        return move

    def minimax_prune_agent(board):
        _, move = agent_prune.minimax_prune(board, 5, float('-inf'), float('inf'), True, 2)
        return move
    
    # Elección de los jugadores
    player_choices = {
        'Random': random_agent,
        'Minimax': minimax_agent,
        'Minimax with Pruning': minimax_prune_agent
    }

    # Interfaz para elegir jugadores
    player1_choice = wn.textinput("Player 1", "Choose a player for Player 1 (Random, Minimax, Minimax with Pruning):")
    player2_choice = wn.textinput("Player 2", "Choose a player for Player 2 (Random, Minimax, Minimax with Pruning):")

    player1 = player_choices.get(player1_choice)
    player2 = player_choices.get(player2_choice)

    if player1 is None or player2 is None:
        print("Invalid player choice. Exiting...")
        return

    # Ejecutar los juegos y calcular estadísticas
    avg_time_player1, avg_time_player2, player1_wins, player2_wins, draws = run_multiple_games(player1, player2, num_games)

    # Mostrar estadísticas y resultados
    results_text = f"Player 1 wins: {player1_wins}\n"
    results_text += f"Player 2 wins: {player2_wins}\n"
    results_text += f"Draws: {draws}\n"
    results_text += f"Average game time for Player 1: {avg_time_player1:.2f} seconds\n"
    results_text += f"Average game time for Player 2: {avg_time_player2:.2f} seconds\n"

    print(results_text)

    # Dibujar gráfico de barras
    draw_bar_chart(player1_wins, player2_wins, draws)

    wn.mainloop()

if __name__ == "__main__":
    main()
