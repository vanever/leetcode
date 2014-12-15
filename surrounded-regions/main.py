class Solution:

  class Point:
    def __init__(self, x, y):
      self.x = x
      self.y = y

  # @param board, a 2D array
  # Capture all regions by modifying the input board in-place.
  # Do not return any value.
  def solve(self, board):
    row = len(board)
    col = 0
    if row > 0:
      col = len(board[0])
    if row <= 0 or col <= 0:
      return

    self.board = board
    self.row = row
    self.col = col

    self.surrounded = [[True for _ in xrange(0, col)] for _ in xrange(0, row)]

    for i in [0, row - 1]:
      for j in xrange(0, col):
        if board[i][j] == 'O':
          self.extendpoint(i, j)

    for j in [0, col - 1]:
      for i in xrange(0, row - 1):
        if board[i][j] == 'O':
          self.extendpoint(i, j)

    for i in range(0, row):
      for j in range(0, col):
        if board[i][j] == 'O' and self.surrounded[i][j]:
          board[i][j] = 'X'

  def extendpoint(self, i, j):
    stack = []
    def tryAddNode(x, y):
      if x >= 0 and x < self.row and y >= 0 and y < self.col and self.board[x][y] == 'O' and self.surrounded[x][y]:
        stack.append(Solution.Point(x, y))
    tryAddNode(i, j)
    while len(stack) > 0:
      p = stack.pop()
      self.surrounded[p.x][p.y] = False
      tryAddNode(p.x-1, p.y)
      tryAddNode(p.x+1, p.y)
      tryAddNode(p.x, p.y-1)
      tryAddNode(p.x, p.y+1)

if __name__ == '__main__':
  s = Solution()
  board = [['O']]
  # board = [
  #     ['X', 'X', 'O', 'X', 'X'],
  #     ['X', 'X', 'X', 'O', 'X'],
  #     ['X', 'X', 'O', 'O', 'X'],
  #     ['O', 'X', 'O', 'O', 'X'],
  #     ['O', 'X', 'X', 'X', 'X'],
  #     ]
  for i in range(0, len(board)):
    print board[i]
  s.solve(board)
  print ''
  for i in range(0, len(board)):
    print board[i]
