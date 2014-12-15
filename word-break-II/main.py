class Solution:

  def __init__(self):
    self.saved = {}

  def wordBreak(self, s, dict):
    self.saved.clear()
    size = len(s)
    return self.wordBreakImpl(s, dict)

  def wordBreakImpl(self, s, dict):
    if s in self.saved:
      return self.saved[s]
    else:
      ret = []
      for i in range(0, len(s)):
        subs = s[0:i+1]
        if subs in dict:
          if (i + 1) == len(s):
            currResult = [s]
          else:
            sentences = self.wordBreakImpl(s[i+1:], dict)
            currResult = map(lambda s: subs + " " + s, sentences)
          ret += currResult

      self.saved[s] = ret
      return ret

if __name__ == '__main__':
  s = Solution()
  dict = set([ "cat", "cats", "sand", "and", "dog" ])
  print s.wordBreak("catsanddog", dict)
