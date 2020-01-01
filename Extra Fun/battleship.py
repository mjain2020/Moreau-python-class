from blessings import Terminal as term
from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)


def print_board(board):
  for row in board:
    print(" ".join(row))


def random_row(board):
  return randint(1, len(board))


def random_col(board):
  return randint(1, len(board[0]))


def get_int(message):
  answer = input(message)
  try:
    int(answer)
  except ValueError:
    while type(answer) != int:
      try:
        answer = int(answer)
      except ValueError:
        answer = input(message)
  return int(answer)


ship_row = random_row(board)
ship_col = random_col(board)

last_message = False

for each_turn in range(4):
  with term().fullscreen():
    term().move(0, 0)
    if last_message:
      print(last_message)
    print("Turn", each_turn + 1)
    print_board(board)

    guess_row = get_int("Guess Row: ")
    guess_col = get_int("Guess Column: ")

  if guess_row == ship_row and guess_col == ship_col:
      print("Congrats, you won!")
      break
  else:
      if (guess_row < 1 or guess_row > len(board)) or (guess_col < 1 or guess_col > len(board[0])):
          last_message = "Oops, that's not even in the ocean."
      elif(board[guess_row - 1][guess_col - 1] == "X"):
          last_message = "You guessed that one already."
      else:
          last_message = "You missed my battleship!"
          board[guess_row - 1][guess_col - 1] = "X"

print("GAME OVER")
print("My battleship was at the %d column and the %d row." %
      (ship_col, ship_row))
