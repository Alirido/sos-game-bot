from random import randint, choice

class Game:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2
    self.player1_scores = 0
    self.player2_scores = 0

  def _checkScore(self, sosboard, row, col):
    total_scores = 0
    if (sosboard.get(row, col) == 'S'):
      if (row < 2):
        if (col < 2):
          total_scores += self._checkRightScore(sosboard, row, col) + self._checkDownScore(sosboard, row, col) + self._checkRightDownScore(sosboard, row, col)
        elif (col > 5):
          total_scores += self._checkLeftScore(sosboard, row, col) + self._checkDownScore(sosboard, row, col) + self._checkLeftDownScore(sosboard, row, col)
        else:
          total_scores += self._checkLeftScore(sosboard, row, col) + self._checkRightScore(sosboard, row, col) + self._checkDownScore(sosboard, row, col) + self._checkLeftDownScore(sosboard, row, col) + self._checkRightDownScore(sosboard, row, col)
      elif (row > 5):
        if (col < 2):
          total_scores += self._checkRightScore(sosboard, row, col) + self._checkUpScore(sosboard, row, col) + self._checkRightUpScore(sosboard, row, col)
        elif (col > 5):
          total_scores += self._checkLeftScore(sosboard, row, col) + self._checkUpScore(sosboard, row, col) + self._checkLeftUpScore(sosboard, row, col)
        else:
          total_scores += self._checkLeftScore(sosboard, row, col) + self._checkRightScore(sosboard, row, col) + self._checkUpScore(sosboard, row, col) + self._checkLeftUpScore(sosboard, row, col) + self._checkRightUpScore(sosboard, row, col)
      else:
        if (col < 2):
          total_scores += self._checkRightScore(sosboard, row, col) + self._checkUpScore(sosboard, row, col) + self._checkDownScore(sosboard, row, col) + self._checkRightUpScore(sosboard, row, col) + self._checkRightDownScore(sosboard, row, col)
        elif (col > 5):
          total_scores += self._checkLeftScore(sosboard, row, col) + self._checkUpScore(sosboard, row, col) + self._checkDownScore(sosboard, row, col) + self._checkLeftUpScore(sosboard, row, col) + self._checkLeftDownScore(sosboard, row, col)
        else:
          total_scores += self._checkLeftScore(sosboard, row, col) + self._checkRightScore(sosboard, row, col) + self._checkUpScore(sosboard, row, col) + self._checkDownScore(sosboard, row, col) + self._checkLeftUpScore(sosboard, row, col) + self._checkLeftDownScore(sosboard, row, col) +  self._checkRightUpScore(sosboard, row, col) + self._checkRightDownScore(sosboard, row, col)
    else:
      if (row == 0 or row == 7):
        if (col > 0 and col < 7):
          total_scores += self._checkRightScore(sosboard, row, col-1)
      else:
        if (col == 0 or col == 7):
          total_scores += self._checkDownScore(sosboard, row-1, col)
        else:
          total_scores += self._checkRightUpScore(sosboard, row+1, col-1) + self._checkRightScore(sosboard, row, col-1) + self._checkRightDownScore(sosboard, row-1, col-1) + self._checkDownScore(sosboard, row-1, col)

    return total_scores

  def _checkUpScore(self, sosboard, row, col):
    if (sosboard.get(row-2, col) == 'S' and sosboard.get(row-1, col) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _checkDownScore(self, sosboard, row, col):
    if (sosboard.get(row+2, col) == 'S' and sosboard.get(row+1, col) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _checkLeftScore(self, sosboard, row, col):
    if (sosboard.get(row, col-2) == 'S' and sosboard.get(row, col-1) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _checkRightScore(self, sosboard, row, col):
    if (sosboard.get(row, col+2) == 'S' and sosboard.get(row, col+1) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _checkLeftUpScore(self, sosboard, row, col):
    if (sosboard.get(row-2, col-2) == 'S' and sosboard.get(row-1, col-1) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _checkRightUpScore(self, sosboard, row, col):
    if (sosboard.get(row-2, col+2) == 'S' and sosboard.get(row-1, col+1) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _checkLeftDownScore(self, sosboard, row, col):
    if (sosboard.get(row+2, col-2) == 'S' and sosboard.get(row+1, col-1) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _checkRightDownScore(self, sosboard, row, col):
    if (sosboard.get(row+2, col+2) == 'S' and sosboard.get(row+1, col+1) == 'O' and sosboard.get(row, col) == 'S'):
      return 1
    return 0

  def _prinScoreBoard(self):
    print("Scoreboard:")
    print(self.player1 + "\t\t", self.player1_scores)
    print(self.player2 + "\t\t", self.player2_scores)

    print()
    if (self.player1_scores > self.player2_scores):
      print("Congratulations, you win!")
    elif (self.player1_scores < self.player2_scores):
      print("You lose. Try again")
    else:
      print("Draw!")

  def play(self, SosBoard):
    isPlayer1Turn = True
    SosBoard.printBoard()
    if (self.player1 == "Player" and self.player2 == "Easy bot"):
      while not(SosBoard.isComplete()):
        if isPlayer1Turn:
          print(">> " + self.player1 + " turn")		
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
          self.player1_scores += self._checkScore(SosBoard, row-1, col-1)
          print()
          print("( " + self.player1 + " scores =", self.player1_scores, ")")
          print()

          isPlayer1Turn = False
        else:
          print(">> " + self.player2 + " turn")
          row = randint(0, 7)
          col = randint(0, 7)
          while (SosBoard.isFilled(row, col)):
            row = randint(0, 7)
            col = randint(0, 7)
					
          act = choice("SO")
          SosBoard.fill(row, col, act)
          self.player2_scores += self._checkScore(SosBoard, row, col)
          print("( " + self.player2 + " scores = ", self.player2_scores, ")")
          print()
          SosBoard.printBoard()

          isPlayer1Turn = True

      self._prinScoreBoard()

