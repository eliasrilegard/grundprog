from p5 import *

class Tile:
  """ The objects that are filled into the main matrix. May contain a mine. Generally the class that does the drawing. """

  def __init__(self,i,j,w):
    self.gridX, self.gridY = i, j                                       # i & j matrix indicies
    self.width = w                                                  # Tile width
    self.screenX, self.screenY = i * w, j * w                               # x & y coordinates on screen
    self.mine, self.flagged = False, False
    self.nearby, self.revealed = 0, False
    self.exploded = False

  def show(self):
    """ When called, the tile is drawn, together with any additional information that shall be presented to user. """

    stroke(0)
    no_fill()
    rect((self.screenX +1, self.screenY), self.width, self.width)                   # Draw rectangle (+1 to fit frame of all tiles)

    if self.revealed:                                           # If tile is marked as revealed
      fill(220)                                                 # Darker background
      if self.exploded:
        fill(255,0,0)
      rect((self.screenX +1, self.screenY), self.width, self.width)                 # Redraw rectangle with new fill color
      if self.nearby > 0:                                       # If neaby count is relevant - write out the number
        fill(0)                                                 
        text(str(self.nearby), (self.screenX + self.width * 0.5, self.screenY + self.width * 0.2))
      if self.mine:
        fill(0)
        ellipse((self.screenX + self.width * 0.5, self.screenY + self.width * 0.5), self.width * 0.5, self.width * 0.5) # Draw the "mine"
    elif self.flagged:
      self.drawFlag()

  def reveal(self):
    self.revealed = True

  def toggleFlag(self):
    self.flagged = not self.flagged

  def drawFlag(self):
    """ Draw a triangle on top of a tile. """

    stroke(0)                                                   # Triangle base
    fill(0)
    triangle((self.screenX + self.width * 0.15, self.screenY + self.width * 0.85),\
             (self.screenX + self.width * 0.5, self.screenY + self.width * 0.65),\
             (self.screenX + self.width * 0.85, self.screenY + self.width * 0.85))

    line((self.screenX + self.width * 0.5, self.screenY + self.width * 0.65), (self.screenX + self.width * 0.5, self.screenY + self.width * 0.15))
    
    stroke(255,0,0)                                             # Red flag
    fill(240,0,0)
    triangle((self.screenX + self.width * 0.5, self.screenY + self.width * 0.15),\
             (self.screenX + self.width * 0.5, self.screenY + self.width * 0.5),\
             (self.screenX + self.width * 0.15, self.screenY + self.width * 0.325))

  def checkCorrect(self,hiddenTiles,correctFlags,incorrectFlags):
    """ Check if the tile is correctly marked. """

    if self.revealed:
      hiddenTiles -= 1
    elif self.flagged:
      if self.mine:
        correctFlags += 1
      else:
        incorrectFlags += 1
    return hiddenTiles, correctFlags, incorrectFlags

  def setMine(self):
    self.mine = True

  def clearMine(self):
    self.mine = False

  def setNearby(self, count):
    self.nearby = count

  def setExploded(self):
    self.exploded = True