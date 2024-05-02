import random
import numpy as np
from checkers.game import Game
import sys
import os
sys.path.append(os.path.abspath(''))
from Minimax import agent_prune

class QlearningAgent:
    def __init__(self, alpha, epsilon, discount, get_possible_actions):
        self.get_possible_actions = get_possible_actions
        # print("get_possible_actions", get_possible_actions)
        self.alpha = alpha
        self.epsilon = epsilon
        self.discount = discount
        try:
            self.q_values = np.load("q_values.npy", allow_pickle=True).item()
        except:
            self.q_values = {}
        self.state = None
    
    def get_q_value(self, state, action):
        return self.q_values.get((state, action), 0)
    
    def get_value(self, board, state):
        possible_actions = self.get_possible_actions(board)
        possible_actions = [tuple(action) for action in possible_actions]
        if len(possible_actions) == 0:
            return 0
        return max([self.get_q_value(state, action) for action in possible_actions])
    
    def save_q_values(self, filename):
        np.save(filename, self.q_values)

    def load_q_values(self, filename):
        self.q_values = np.load(filename, allow_pickle=True).item()
    
    def get_best_action(self, board, state):
        possible_actions = self.get_possible_actions(board)
        possible_actions = [tuple(action) for action in possible_actions]
        if len(possible_actions) == 0:
            return None
        return max(possible_actions, key=lambda a: self.get_q_value(state, a))
    
    def get_action(self, board, state):
        possible_actions = self.get_possible_actions(board)
        possible_actions = [tuple(action) for action in possible_actions]
        if len(possible_actions) == 0:
            return None
        if random.random() < self.epsilon:
            return random.choice(possible_actions)
        return self.get_best_action(board, state)
    
    def update(self, state, action, reward, board, next_state):
        # print('next_state', next_state, 'action', action, 'reward', reward)
        next_value = self.get_value(board, next_state)
        self.q_values[(state, action)] = self.get_q_value(state, action) + self.alpha * (reward + self.discount * next_value - self.get_q_value(state, action))

    def random_player(board):
        move = random.choice(board.get_possible_moves())
        return move
    
    #train the agent with minimax
    def train_with_minimax(self, depth, num_episodes):
        print("training with minimax")
        counter = 0
        try:
            self.load_q_values("q_values.npy")
            print("Loaded Q values from file.")
        except:
            print("No previous Q values found. Starting from scratch.")
        for _ in range(num_episodes):
            game = Game()
            state = game.board.searcher.player_positions
            state = tuple(tuple(vals) for vals in state.values())
            print("counter", counter)
            counter += 1

            while not game.is_over() and game.get_winner() == None:
                if game.whose_turn() == 1 :
                    action = self.get_action(game.board, state)
                else:
                    print("possible moves minimax:::", game.board.get_possible_moves())
                    evaluation, action = agent_prune.minimax_prune(game, depth, float('-inf'), float('inf'), True, 2)
                    print("action_minimax", action)
                    action = tuple(action)
                game.move(list(action))
                next_state = game.board.searcher.player_positions
                next_state = tuple(tuple(vals) for vals in next_state.values())
                reward = 0 if not game.is_over() else 1
                self.update(state, action, reward, game.board, next_state)
                state = next_state
            
            print("winner", game.get_winner())
        print("q_values", self.q_values)
        self.save_q_values("q_values.npy")
    
    def play(self, game):
        state = game.board.searcher.player_positions
        while not game.is_over():
            action = self.get_best_action(game.board, state)
            game.move(list(action))
            state = game.board
        return game.get_winner()
    
    def play_against_minimax(self, game, depth):
        state = game.board.searcher.player_positions
        state = tuple(tuple(vals) for vals in state.values())
        while not game.is_over() and game.get_winner() == None:
            if game.whose_turn() == 1:
                action = self.get_best_action(game.board, state)
            else:
                evaluation, action = agent_prune.minimax_prune(game, depth, float('-inf'), float('inf'), True, 2)
            game.move(list(action))
            state = game.board
        return game.get_winner()
    
    def calculate_win_rate(self, game, num_episodes):
        wins = 0
        for _ in range(num_episodes):
            game = Game()
            winner = self.play_against_minimax(game, 5)
            if winner == 1:
                wins += 1
        return wins / num_episodes
    


if __name__ == "__main__":
    game = Game()

    agent = QlearningAgent(0.5, 0.1, 0.9, lambda board: board.get_possible_moves())
    print("Training agent...", agent)
    agent.train_with_minimax(5, 1000)  # Llama a la función de entrenamiento
    print("training has finished")
    win_rate = agent.calculate_win_rate(game, 1000)
    print("Win rate against Minimax:", win_rate)
    agent.save_q_values("q_values.npy")

