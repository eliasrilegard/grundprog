import random, tile, helpers

class Board:
  """ A bigger class containing any and all relevant data that's required for the game to run. """

  def __init__(self):
    self.correctFlags, self.incorrectFlags = 0, 0
    self.gameOver, self.didWin = False, None
    self.ready = False

  def update(self,cols,rows,mineCount,tileWidth):
    self.cols, self.rows = cols, rows
    self.matrix = helpers.create2DArray(cols,rows)              # This is the matrix that holds the tiles
    self.hiddenTiles = cols * rows
    self.mineCount = mineCount

    for i in range(cols):
      for j in range(rows):
        self.matrix[i][j] = tile.Tile(i,j,tileWidth)            # Place a tile object in every slot in the matrix
    self.ready = True
    

  def show(self):                                               # Show board - i.e show all tiles
    """ Loop through every tile, showing them in the process. Also checks the win condition. """

    self.hiddenTiles = self.cols * self.rows
    self.correctFlags, self.incorrectFlags = 0, 0
    for i in range(self.cols):
      for j in range(self.rows):
        self.matrix[i][j].show()
        self.hiddenTiles, self.correctFlags, self.incorrectFlags = self.matrix[i][j].checkCorrect(self.hiddenTiles, self.correctFlags, self.incorrectFlags)
        if self.hiddenTiles == self.mineCount or self.correctFlags == self.mineCount and self.incorrectFlags == 0:
          self.gameOver = True                                  # Game over, win
          self.didWin = True

  def constructMines(self):
    """ Randomize mine placement. """

    placedMines = 0
    while placedMines < self.mineCount:                         # I.e place mineCount amout of mines
      i = random.randint(0,self.cols -1)                        # Random coordinates
      j = random.randint(0,self.rows -1)
      if not self.matrix[i][j].mine:                            # Can't place a mine on an already occupied tile
        self.matrix[i][j].setMine()
        placedMines += 1                                        

  def locateMines(self):
    """ Check how many adjacent mines exists for every tile. """

    for i in range(self.cols):                                  # Check all mines
      for j in range(self.rows):
        if self.matrix[i][j].mine:                              # Set nearby count of a mine to -1
          self.matrix[i][j].setNearby(-1)
          continue
        count = 0
        for dx in range(-1,1 +1):                               # Check all surrounding tiles of current tile
          for dy in range(-1,1 +1):
            if -1 < i + dx < self.cols and -1 < j + dy < self.rows: # Check we are still inside board coordinates
              if self.matrix[i + dx][j + dy].mine:
                count += 1
        self.matrix[i][j].setNearby(count)                      # Set neaby count to however many mines was found

  def revealTile(self,i,j):
    """ Mark tile as revealed and check if game is lost, if user has clicked on a mine. """

    if not self.matrix[i][j].flagged:                           # Don't reveal a tile if the tile is flagged
      self.matrix[i][j].reveal()
      if self.matrix[i][j].nearby == 0:                         # If nearby count is 0
        self.floodFill(self.matrix[i][j])                       # Flood fill time
      elif self.matrix[i][j].mine:
        self.matrix[i][j].setExploded()
        self.revealMines()
        self.gameOver = True                                    # Game over, lost
        self.didWin = False

  def revealMines(self):
    """ Reveal all mines on the board. """

    for i in range(self.cols):
      for j in range(self.rows):
        if self.matrix[i][j].mine:                              # Only reveal mines
          self.matrix[i][j].reveal()

  def checkReplace(self,i,j):
    """ Given a tile, check that no mines are adjacent to it. If a mine is found, redo mine placement. """

    replace = True
    while replace:                                              # Keep looping
      replace = False                                           # Assume no mines are found
      for dx in range(-1,1 +1):                                 # Iterate around tile coordinates
        for dy in range(-1,1 +1):
          if -1 < i + dx < self.cols and -1 < j + dy < self.rows: # Still inside board bounds?
            if self.matrix[i + dx][j + dy].mine:                # If a mine is found, set replace to true
              replace = True
      if replace:
        for x in range(self.cols):                              # If need to replace, clear all mines, then replace
          for y in range(self.rows):
            self.matrix[x][y].clearMine()
        self.constructMines()
        self.locateMines()                                      # Update tile numbers

  def flagTile(self,i,j):
    self.matrix[i][j].toggleFlag()

  def floodFill(self,tile):
    """ Reveal all tiles around a given tile. """
    for dx in range(-1,1 +1):                                   # Iterate around tile
      for dy in range(-1,1 +1):
        if -1 < tile.gridX + dx < self.cols and -1 < tile.gridY + dy < self.rows: # Check if we are still within board bounds
          neighbor = self.matrix[tile.gridX + dx][tile.gridY + dy]
          if not neighbor.revealed and not neighbor.mine:       # Want to modify tiles that are hidden and not a mine
            self.revealTile(neighbor.gridX,neighbor.gridY)
          del neighbor                                          # TODO: Check if this is good to use