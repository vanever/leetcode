class Solution:
  # @param s, a string
  # @return a list of lists of string
  def partition(self, s):
    self.cache = {}
    return self.partitionRec(s)

  def partitionRec(self, s):
    if len(s) == 0:
      return []
    if s in self.cache:
      return self.cache[s]
    else:
      ret = []
      if self.isPalindrome(s):
        ret.append([s])
      size = len(s)
      for i in xrange(1, size):
        xs = s[0:i]
        if self.isPalindrome(xs):
          def mergeToList(p):
            xp = list(p)
            xp.insert(0, xs)
            return xp
          ret += map(mergeToList, self.partitionRec(s[i:]))
      self.cache[s] = ret
      return ret

  def isPalindrome(self, s):
    assert len(s) > 0
    i = 0
    j = len(s) - 1
    while i < j and s[i] == s[j]:
      i += 1
      j -= 1
    return i >= j

if __name__ == '__main__':
  s = Solution()
  print s.partition("aab")
