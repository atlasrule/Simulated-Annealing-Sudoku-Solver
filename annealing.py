from boxes import next_state
from fitness import score
from numpy import clip, exp, random, std
from copy import deepcopy

# Calculates initial temperature for annealing process.
def calculateInitialTemperature(board, immutable_positions):

  scores = []

  for i in range(10):

    board = next_state(board, immutable_positions)

    scores.append(score(board))

  return std(scores) - 1


# Starts the annealing process for given sudoku board
def solve(board, immutable_positions):
  iter = 0
  n_reheats = 0
  temperature = initialTemperature = calculateInitialTemperature(board, immutable_positions)
  cooling_rate = 0.99

  board_score = score(board)

  old_board = deepcopy(board)

  while score(board) >= 1:
    stuckCount = 0

    for i in range(  int(iter/10)+1  ):

        
      if board_score < 5:
        if board_score <= 0:
          break
        stuckCount += 1

      if stuckCount > 300:
        stuckCount = 0
        temperature = initialTemperature
        n_reheats += 1
    
      board = next_state(board, immutable_positions)
      
      board_score = score(board)
      # print('Iteration: {}, Temperature: {},  Score: {}'.format( iter, temperature, board_score))
  
      delta_f =  board_score - score(old_board)
      #print('Iteration: {}, Temperature: {},  Board Score {}, stuckCount {}'.format( iter, temperature, board_score, stuckCount))
  
      if random.uniform(1,0,1) > exp(-delta_f/temperature):
        # Do not accept
        board = deepcopy(old_board)
        iter += 1
        continue
      #print('Iteration: {}, Temperature: {},  Score: {}'.format( iter, temperature, board_score))

      iter += 1
      temperature = temperature * cooling_rate
      old_board = deepcopy(board)
  
  #print('Iteration:', iter, ', Fitness score: ', score(board))
 
  #print('n_reheats', n_reheats)
  return board
