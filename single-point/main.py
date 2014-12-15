class Solution:
  def singleNumber(self, A):
    ret = 0
    for i in A:
      ret ^= i
    return ret
