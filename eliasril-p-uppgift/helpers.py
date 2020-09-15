def create2DArray(cols, rows):
  """ Creates and returns a matrix. """
  arr = [None] * cols
  for i in range(cols):
    arr[i] = [None] * rows
  return arr