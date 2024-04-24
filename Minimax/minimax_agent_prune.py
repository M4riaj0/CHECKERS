import random
from checkers.game import Game
import time

def minimax_prune(game, depth, max_player, alpha, beta):
  global ct
  board = game.board
  if depth == 0 or game.is_over():
    return score_count(board), None

  moves = board.get_possible_moves()
  random.shuffle(moves)

  if max_player:
    max_eval = -float('Inf')
    for move in moves:
      board.push(move)
      ct += 1
      current_eval, cur_move = minimax_prune(board, depth-1, False, alpha, beta)
      board.pop()
      if current_eval > max_eval:
        max_eval = current_eval
        best_move = move
        alpha = max(alpha, max_eval)
        if beta <= alpha:
          break
    return max_eval, best_move
  else:
    min_eval = float('Inf')
    for move in moves:
      board.push(move)
      ct += 1
      current_eval, cur_move = minimax_prune(board, depth-1, True, alpha, beta)
      board.pop()
      if current_eval < min_eval:
        min_eval = current_eval
        best_move = move
        beta = min(alpha, min_eval)
        if beta <= alpha:
          break
    return min_eval, best_move
  
def score_count(board):
    score = 0
    pass