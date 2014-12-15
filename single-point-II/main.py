class Solution:
  def singleNumber(self, A):
    bit1 = 0
    bit2 = 0
    for i in A:
      nbit1 = (i ^ bit1) & ~bit2
      bit2 = (~bit1 & bit2 & ~i) | (bit1 & ~bit2 & i)
      bit1 = nbit1
    return bit1

if __name__ == '__main__':
  a = [1,2,1,1,2,2,3]
  print Solution().singleNumber(a)
