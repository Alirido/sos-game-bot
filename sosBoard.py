class SosBoard:
  def __init__(self):
    self.board = [['_' for _ in range(8)] for _ in range(8)]
    self.count = 0

  def fill(self, row, col, act):
  	self.board[row][col] = act
  	self.count += 1

  def get(self, row, col):
  	return self.board[row][col]

  def isComplete(self):
  	return self.count == 64

  def isFilled(self, row, col):
  	return self.board[row][col] != '_'

  def printBoard(self):
  	print("----- SOS board -----")
  	print()
  	for i in range(8):
  		for j in range(8):
  			print(self.board[i][j], end=' ')
  		print()
  	print()