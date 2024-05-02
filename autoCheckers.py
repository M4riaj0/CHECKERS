import statistics
import matplotlib.pyplot as plt
from checkers.game import Game
from Random.random_agent import random_player
from Minimax import agent, agent_prune
from copy import deepcopy #With this we can copy the game object
from Qlearning.q_agent import QlearningAgent
import random
import time

def run_game():
    q_agent = QlearningAgent(0.5, 0.1, 0.9, lambda board: board.get_possible_moves())
    game = Game()
    print("game has started")
    player1_time = 0
    player2_time = 0
    # print("winner::", game.get_winner())
    while not game.is_over() and game.get_winner() == None:
        # print("game turn::", game.whose_turn())
        if game.whose_turn() == 1:
            start_time = time.time()
            # move for random player
            # move = random_player(game)

            # move for q_agent
            # state = game.board.searcher.player_positions
            # state = tuple(tuple(vals) for vals in state.values())
            # move = q_agent.get_action(game.board, state)
            # move = list(move)

            # move for minimax with alpha beta pruning
            # _, move = agent_prune.minimax_prune(game,5, float('-inf'), float('inf'), True, 1)
            # print("move from minimax::", move)
            # move for minimax 
            _, move = agent.minimax(game,3, True, 1)

            end_time = time.time()
            player1_time += end_time - start_time
        else:
            start_time = time.time()
            # move for random player
            # move = random_player(game)
            # print("move from random::", move)

            # move for minimax with alpha beta pruning
            _, move = agent_prune.minimax_prune(game,5, float('-inf'), float('inf'), True, 2)

            # move for minimax 
            # _, move = agent.minimax(game,3, True, 2)
            end_time = time.time()
            player2_time += end_time - start_time
        # print("winner::", game.get_winner())
        # print("pieces::", game.board.searcher.player_positions)
        game.move(move)
    print("winner::", game.get_winner())
    return player1_time, player2_time, game.get_winner()

# Función para ejecutar múltiples juegos y calcular estadísticas
def run_multiple_games(max_num_games):
    win_percentages_player1 = []
    win_percentages_player2 = []
    draw_percentages = []
    
    # Ejecutar los juegos para cada cantidad de juegos en el rango especificado
    for num_games in range(10, max_num_games + 1, 10):
        total_wins_player1 = 0
        total_wins_player2 = 0
        total_draws = 0
        
        # Ejecutar los juegos para la cantidad actual de juegos
        for _ in range(num_games):
            _, _, winner = run_game()
            if winner == 1:
                total_wins_player1 += 1
            elif winner == 2:
                total_wins_player2 += 1
            else:
                total_draws += 1
        
        # Calcular los porcentajes
        win_percentage_player1 = (total_wins_player1 / num_games) * 100
        win_percentage_player2 = (total_wins_player2 / num_games) * 100
        draw_percentage = (total_draws / num_games) * 100
        
        # Almacenar los porcentajes en listas
        win_percentages_player1.append(win_percentage_player1)
        win_percentages_player2.append(win_percentage_player2)
        draw_percentages.append(draw_percentage)
    
    return win_percentages_player1, win_percentages_player2, draw_percentages



# Función para dibujar el desempeño de los jugadores de manera lineal
def draw_performance_chart(max_num_games, win_percentages_player1, win_percentages_player2, draw_percentages):
    num_games_list = list(range(10, max_num_games + 1, 10))
    plt.plot(num_games_list, win_percentages_player1, label='minimax Wins')
    plt.plot(num_games_list, win_percentages_player2, label='minimax_prune Wins')
    plt.plot(num_games_list, draw_percentages, label='Draws')
    plt.xlabel('Number of Games')
    plt.ylabel('Percentage')
    plt.title('Player Performance')
    plt.legend()
    plt.show()

# Función principal
def main():
    max_num_games = 50  # Número máximo de juegos a jugar
    
    # Ejecutar los juegos y calcular estadísticas
    win_percentages_player1, win_percentages_player2, draw_percentages = run_multiple_games(max_num_games)
    
    # Mostrar resultados y graficar
    draw_performance_chart(max_num_games, win_percentages_player1, win_percentages_player2, draw_percentages)

if __name__ == "__main__":
    main()
