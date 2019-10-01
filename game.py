from random import randint, choice

class Game:
	def __init__(self, player1, player2):
		self.player1 = player1
		self.player2 = player2

	def play(self, SosBoard):
		isPlayer1Turn = True
		SosBoard.printBoard()
		if (self.player1 == "Player" and self.player2 == "Easy bot"):
			while not(SosBoard.isComplete()):
				if isPlayer1Turn:
					print("-> " + self.player1 + " turn")		
					row = int(input("Choose row: "))
					while row < 1 or row > 8:
						print("# Row must be number 1-8")
						row = int(input("Choose row: "))
					
					col = int(input("Choose column: "))
					while col < 1 or col > 8:
						print("# Column must be number 1-8")
						col = int(input("Choose column: "))

					while (SosBoard.isFilled(row-1, col-1)):
						print("Cell has been filled, choose another cell")
						row = int(input("Choose row: "))
						while row < 1 or row > 8:
							print("# Row must be number 1-8")
							row = int(input("Choose row: "))
						
						col = int(input("Choose column: "))
						while col < 1 or col > 8:
							print("# Column must be number 1-8")
							col = int(input("Choose column: "))

					act = input("Choose S or O: ")
					while act != 'S' and act != 'O':
						print("# Input must be S or O")
						act = input("Choose S or 0: ")

					SosBoard.fill(row-1, col-1, act)
					print()

					isPlayer1Turn = False
				else:
					print("-> " + self.player2 + " turn")
					row = randint(0, 7)
					col = randint(0, 7)
					while (SosBoard.isFilled(row, col)):
						row = randint(0, 7)
						col = randint(0, 7)
					
					act = choice("SO")
					SosBoard.fill(row, col, act)

					SosBoard.printBoard()

					isPlayer1Turn = True

