# Defined every 3x3 blocks of the classic sudoku board as a "box".
# This script includes operations like filling, picking and swapping values across boxes.

from random import choice, randint


def box_coordinates(x,y):
  boxX = x // 3
  boxY = y // 3
  return boxX, boxY

def random_cell_in_box(boxX, boxY):
  x_end = (boxX+1) * 3 - 1
  x_start = x_end - 2

  y_end = (boxY+1) * 3 - 1
  y_start = y_end - 2

  randomX = randint(x_start, x_end)
  randomY = randint(y_start, y_end)
  return randomX, randomY


def box_data_index(boxX, boxY):
  return boxX * 3 + boxY


def add_to_box_data(box_data, x,y, value):
  idx = box_data_index( *box_coordinates(x,y) )
  box_data[idx].add(value)


def get_box_data(box_data, x,y):
  idx = box_data_index( *box_coordinates(x,y) )
  return box_data[idx]


def possible_random(box_data, x,y):
  all_digits = [i for i in range(1,10)]
  s = set( get_box_data(box_data, x,y) )
  possible = [x for x in all_digits if x not in s]
  return choice(possible)


def create_given_box_data(board):
  box_data = [set() for i in range(9)] 
  for i in range(9):
    for j in range(9):
      value = board[i][j]
      if value != 0:
        add_to_box_data(box_data, i,j, value)
  return box_data


def random_fill_boxes(board):
  # Function fills all empty cells of 3x3 boxes with a missing random value
  box_data = create_given_box_data(board)
  for i in range(9):
    for j in range(9):
      if board[i][j] == 0:
        random_value = possible_random(box_data, i,j)
        board[i][j] = random_value
        add_to_box_data(box_data, i,j, random_value)


def pick_random_box():
  return randint(0,2), randint(0,2)


def pick_random_cell(board, boxX, boxY, immutable_positions):
  x,y = random_cell_in_box(boxX, boxY)
  first_try = 1
  while (x,y) in immutable_positions or first_try:
    if first_try:
      first_try = 0
    x,y = random_cell_in_box(boxX, boxY)
  return x, y


def swap_values(board, first_cell, second_cell):
  x1,y1, x2,y2 = *first_cell, *second_cell
  temp = board[x1][y1]
  board[x1][y1] = board[x2][y2]
  board[x2][y2] = temp
  return board


def next_state(board, immutable_positions):
  first_box_x, first_box_y = pick_random_box()
  first_random_cell = pick_random_cell(board, first_box_x, first_box_y, immutable_positions)
  second_random_cell = (0,0)
  first_try = 1
  while second_random_cell == first_random_cell or first_try:
    if first_try:
      first_try = 0
    second_random_cell = pick_random_cell(board, first_box_x, first_box_y, immutable_positions)
  board = swap_values(board, first_random_cell, second_random_cell)
  return board