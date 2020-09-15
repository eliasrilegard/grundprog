from p5 import *
import time, board, scoremanager

matrix = None
scoreManager = None
cols, rows = 0, 0
tileWidth = 50
totalMines = 0
tStart = time.time()

def setup():
  """ Function that runs once and sets up any prerequisites before draw initializes. """

  title("Minesweeper by Elias Rilegård")
  size(700,700) 
  #no_loop()                              

  font = create_font("Arial.ttf", tileWidth // 2)                       # Scale font to cell width (tested with w = 30, 40)
  text_font(font)
  text_align(CENTER)

  global scoreManager
  scoreManager = scoremanager.ScoreManager(tStart)

  global matrix
  matrix = board.Board()

def draw():
  """ Runs and repeats continuously. The "driver" function that displays everything. """

  background(255)

  if not scoreManager.gameBegun:
    scoreManager.showPreGame()
  elif not matrix.gameOver and matrix.ready:                    # While not game over:
    matrix.show()                                               # display game
  elif matrix.gameOver and not scoreManager.updated:            # If game has ended and scoreManager isn't updated
    scoreManager.update(time.time(),matrix.didWin,matrix.hiddenTiles,matrix.correctFlags) # Send updated values to scoreManager
  elif scoreManager.updated:
    scoreManager.showGameEnd()                                  # Show scoreManager screen

def mouse_pressed():
  """ Runs whenever the mouse is clicked. Used by user to interact with sketch. """

  i = int(mouse_x // tileWidth)                                         # Calculate coordinates to get tile pressed
  j = int(mouse_y // tileWidth)
  if matrix.hiddenTiles == cols * rows:
    matrix.checkReplace(i,j)
  matrix.revealTile(i,j)                                        # Reveal pressed tile

def key_pressed():
  """ Runs whenever any key is clicked. Used by the user to interact with sketch. """

  if not scoreManager.gameBegun:
    if str(key) in "1234567890":
      scoreManager.tempNumber += str(key)
    elif key == "ENTER":
      scoreManager.confirm()
    redraw()
  elif not scoreManager.returned:
    cols, rows, totalMines = scoreManager.passBack()
    size(cols * tileWidth, rows * tileWidth)

    matrix.update(cols,rows,totalMines,tileWidth)
    matrix.constructMines()
    matrix.locateMines()
    #loop()

  elif not matrix.gameOver:                                       # While in game
    if key == " ":                                              # If spacebar is pressed
      i = int(mouse_x // tileWidth)
      j = int(mouse_y // tileWidth)
      matrix.flagTile(i,j)
  else:                                                         # While on scoreManager screen
    if key == "BACKSPACE":
      scoreManager.name = scoreManager.name[:-1]
    elif key not in ["SHIFT","META","CONTROL","ALT","TAB","ENTER"]: # Exclude these to make it easier for user to enter name
      scoreManager.name += str(key)
    elif key == "ENTER":                                        # Once the user presses enter, update the highscore file
      scoreManager.updateFile()

if __name__ == "__main__":
  run()