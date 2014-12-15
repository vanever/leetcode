class Solution:
  # @param s, a string
  # @return an integer
  def minCut(self, s):
    size = len(s)
    if size <= 1:
      return 0

    self.isPalin = [[False for _ in range(0, size)] for _ in xrange(0, size)]

    for i in xrange(0, size):
      self.isPalin[i][i] = True

    for i in xrange(1, size):
      for j in xrange(0, size - i):
        if s[j] == s[j+i]:
          self.isPalin[j][j+i] = self.isPalin[j+1][j+i-1] if i > 1 else True
        else:
          self.isPalin[j][j+i] = False

    mins = [100000000 for _ in xrange(0, size)]

    for i in xrange(0, size):
      if self.isPalin[0][i]:
        mins[i] = 0
      else:
        for j in xrange(1, i+1):
          if self.isPalin[j][i]:
            mins[i] = min(mins[i], mins[j-1] + 1)

    return mins[size - 1]

if __name__ == '__main__':
  s = Solution()
  print s.minCut("aab")
  assert s.minCut("aab") == 1
  print s.minCut("aa")
  assert s.minCut("aa") == 0
  print s.minCut("aabb")
  assert s.minCut("aabb") == 1
  print s.minCut("abba")
  assert s.minCut("abba") == 0
  print s.minCut("abcd")
  assert s.minCut("abcd") == 3
  print s.minCut("abzzcd")
  assert s.minCut("abzzcd") == 4
  print s.minCut("cabababcbc")
  assert s.minCut("cabababcbc") == 3
