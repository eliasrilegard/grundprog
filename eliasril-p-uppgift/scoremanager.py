from p5 import *
import helpers

class ScoreManager:
  """ Screen display results and get user name, as well as managing the highscore list. """

  def __init__(self,timeStart):
    self.updated = False
    self.name = ""
    self.timeStart = timeStart
    self.gameBegun = False
    self.returned = False
    self.tempNumber = ""
    self.cols, self.rows, self.mineCount = 0,0,0

  def update(self,timeEnd,didWin,hiddenTiles,correctFlags):
    """ Basically a second __init__, parsing updated values. """

    self.updated = True
    self.didWin = didWin
    self.timeEnd = timeEnd
    self.hiddenTiles = hiddenTiles
    self.correctFlags = correctFlags

  def showPreGame(self):
    """ The main menu, where the user can enter how many columns, rows and mines they want. Not very pretty though. """

    stroke(0)
    fill(0)

    text("Click a tile to open it. Press space to mark with a flag.", (width / 2, height * 0.1))
    text("Enter # cols:", (width / 2, height * 0.25))
    text(str(self.cols), (width / 2, height * 0.3))

    if self.cols != 0:
      text("Enter # rows:", (width / 2, height * 0.4))
      text(str(self.rows), (width / 2, height * 0.45))

      if self.rows != 0:
        text("Enter # mines:", (width / 2, height * 0.55))
        text(str(self.mineCount), (width / 2, height * 0.6))

  def confirm(self):
    """ Switches the value that tempNumber is modifying """

    if self.cols == 0:
      self.cols = int(self.tempNumber)
      self.tempNumber = ""
    elif self.rows == 0:
      self.rows = int(self.tempNumber)
      self.tempNumber = ""
    elif self.mineCount == 0:
      self.mineCount = int(self.tempNumber)
      self.gameBegun = True

  def passBack(self):
    self.returned = True
    return self.cols, self.rows, self.mineCount

  def showGameEnd(self):                                        # Some text lines telling the user if they won or not
    """ Some text lines informing the user on how the game went, as well as displaying their score and asking for their name. """

    stroke(0)
    fill(0)

    if self.didWin:
      text("You win!", (width / 2, height * 0.3))
    else:
      text("Game over!", (width / 2, height * 0.3))
      text("Correctly flagged mines: {}".format(self.correctFlags), (width / 2, height * 0.37))
    
    diff = self.timeEnd - self.timeStart                        # Time the user took til game ended
    text("Time: {:.2f}".format(diff), (width / 2, height * 0.5))# Display

    self.score = int(100 * self.mineCount / (self.cols * self.rows) * (self.cols * self.rows - self.hiddenTiles) - 2 * diff)
    if self.score < 0:                                          # < We can't have a negative score, ^ Calculate score
      self.score = 0
    text("Score: {:d}".format(self.score),(width / 2, height * 0.8))

    text("Enter your name below", (width / 2, height * 0.6))
    text(self.name, (width / 2, height * 0.7))                  # self.name stores the string the user has entered

  def updateFile(self):                                         # Once the user has entered their name, update the high score list
    """ Import the highscore data from a file, compare the user's result with stored ones. If better, sort list and write back into file. """

    newlines = []                                               # Store outside to access from other open line?
    with open("highscore.txt") as f:
      scoreMatrix = helpers.create2DArray(11,2)                 # [[None, None],[None, None],...,[None,None]]
      lines = f.readlines()

      for i in range(10):
        line = lines[i][lines[i].find(" ") +1:].split()         # Each line is a list of words
        scoreMatrix[i][0] = int(line[-1])                       # Score imported from text file
        scoreMatrix[i][1] = " ".join(line[:-1])                 # Name, effectively what's remaining from line

      scoreMatrix[10][0] = self.score                           # Set user score and name
      scoreMatrix[10][1] = self.name

      for i in range(len(scoreMatrix)):                         # Bubble sort, placing the lowest score at the end
        for j in range(len(scoreMatrix) -1):
          if scoreMatrix[j][0] < scoreMatrix[j+1][0]:
            scoreMatrix[j], scoreMatrix[j+1] = scoreMatrix[j+1], scoreMatrix[j]
      
      scoreMatrix.pop(-1)                                       # Remove the lowest score, as well as the corresponding name

      for i in range(len(scoreMatrix)):
        newlines.append("{}. {} {}".format(i+1, scoreMatrix[i][1], scoreMatrix[i][0]))  # Fancy stuff (1. Name score)

    with open("highscore.txt","w") as f:                        # Open in write mode
      f.write("\n".join(newlines))                              # Overwrite file
    exit()