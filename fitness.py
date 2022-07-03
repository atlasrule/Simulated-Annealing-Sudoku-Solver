# Calculates fitness of the board.
# For sudoku problem I have define fitness as a minimization value. So 0 fitness means puzzle has solved.
# We calculate sum of each row and column number repetitions. Less repetitions means closer we get to the global solution.  

def sum_of_row_duplicates(board):
  sum = 0
  for row in board:
    sum += len(row) - len(set(row))
  return sum


def sum_of_column_duplicates(board):
  sum = 0
  column = []
  for j in range(9):
    column.clear()
    for i in range(9):
      column.append(board[i][j])
    sum += len(column) - len(set(column))
  return sum


def score(board):
  return sum_of_row_duplicates(board) + sum_of_column_duplicates(board)