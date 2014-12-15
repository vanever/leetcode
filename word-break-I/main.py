class Solution:

  # @param s, a string
  # @param dict, a set of string
  # @return a boolean
  def wordBreak(self, s, dict):
    self.cache = {}
    return self.wordBreakImpl(s, dict)

  def wordBreakImpl(self, s, dict):
    if s in self.cache:
      return self.cache[s]
    ok = False
    for i in range(0, len(s)):
      substr = s[0:len(s)-i]
      if substr in dict:
        if i != 0:
          ok = self.wordBreakImpl(s[-i:], dict)
        else:
          ok = True
        if ok:
          break
    self.cache[s] = ok
    return ok


if __name__ == '__main__':
  print Solution().wordBreak("aaaaaaa", set(["aaaa", "aaa"]))
