from sosBoard import SosBoard
from game import Game
import sys

if __name__ == "__main__":
  print()
  print("WELCOME TO SOS GAME!")
  print("____________________")
  SosBoard = SosBoard()

  print()
  print("Game mode:")
  print("1. Player vs CPU (Hard)")
  print("2. Player vs CPU (Easy)")
  print("3. CPU (Hard) vs CPU (Easy)")
  print("0. Exit")
  mode = int(input("What mode do you wanna play? "))
  while mode not in [0, 1, 2, 3]:
    print("Invalid mode, try again")
    print()
    print("Game mode:")
    print("1. Player vs CPU (Hard)")
    print("2. Player vs CPU (Easy)")
    print("3. CPU (Hard) vs CPU (Easy)")
    print("0. Exit")
    mode = input("What mode do you wanna play? ")

  if mode == 1:
  	player1 = "Player"
  	player2 = "Hard bot"
  elif mode == 2:
  	player1 = "Player"
  	player2 = "Easy bot"
  elif mode == 3:
  	player1 = "Hard bot"
  	player2 = "Easy bot"
  else:
    print()
    print("See you again :)")
    sys.exit()
  print()
  Game = Game(player1, player2)
  Game.play(SosBoard)

  print("Finish!")