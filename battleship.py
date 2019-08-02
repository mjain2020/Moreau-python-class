from random import randint
from curses import initscr

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print("Welcome to Battleship!")

def random_row(board):
  return randint(1, len(board))

def random_col(board):
  return randint(1, len(board[0]))

def get_input(message, dtype=int):
  a = input(message)
  while type(a) != dtype:
    print("Please enter the correct value!")
    a = input(message)
  return a

def clear_terminal():
  initscr().clear()

ship_row = random_row(board)
ship_col = random_col(board)

for each_turn in range(4):
  print ("Turn", each_turn + 1)
  print_board(board)

  guess_row = get_input("Guess Row: ")
  guess_col = get_input("Guess Column: ")

  if guess_row == ship_row and guess_col == ship_col:
    print ("Congrats, you won!")
    break
  else:
    if (guess_row < 1 or guess_row > len(board)) or (guess_col < 1 or guess_col > len(board[0])):
      print ("Oops, that's not even in the ocean.")
    elif(board[guess_row - 1][guess_col - 1] == "X"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row - 1][guess_col - 1] = "X"
  
  if each_turn == 3:
    print ("GAME OVER")
    print ("My battleship was at the %d column and the %d row." % (ship_col, ship_row) )
  
  
