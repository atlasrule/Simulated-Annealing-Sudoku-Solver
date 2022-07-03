from random import randint, shuffle
from boxes import random_fill_boxes
from annealing import solve
from fitness import score


def create_board():
  board = [ [0]*9 for i in range(9)]
  return board

# Creates a random valid sudoku puzzle to make testing easier.
def create_puzzle(board):
  values = [i for i in range(0,9)]
  immutable_positions = []
  shuffle(values)
  for i in range(9):
    board[i][values[i]] = randint(1,9)
    immutable_positions.append( (i, values[i]) )
  return immutable_positions


def print_board(board, margin=5):
  temp_board = board
  i=0
  print(margin*' '+'╔═══════╤═══════╤═══════╗')
  for line in temp_board:
    line_with_spaces = [(value if value != 0 else ' ') for value in line]
    print("{}║ {} {} {} │ {} {} {} │ {} {} {} ║".format( margin*' ', *line_with_spaces))
    i += 1
    if i % 3 == 0 and i < 8:
      print(margin*' '+'╟───────┼───────┼───────╢')
  print(margin*' '+'╚═══════╧═══════╧═══════╝  ')


def main():
  # Creates the board and assigns some immutable given values
  board = create_board()
  immutable_positions = create_puzzle(board)
  print_board(board)
  print('      Fitness score:', str(score(board)).rjust(3, ' '), '\n\n')

  # Fills all empty cells of 3x3 boxes with a missing random value
  random_fill_boxes(board)

  board = solve(board, immutable_positions)
  print_board(board)
  print('      Fitness score:', str(score(board)).rjust(3, ' '))


if __name__ == '__main__':
  main()