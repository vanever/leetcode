class Solution:
  # @param num, a list of integer
  # @return an integer
  def findPeakElement(self, num):
    return self.findPeakElementRange(num, 0, len(num) - 1)

  def findPeakElementRange(self, num, i, j):
    assert i <= j
    if j == i:
      return j
    elif j == i + 1:
      return j if num[j] > num[i] else i
    else:
      m = i + (j - i) / 2
      assert m > i and m < j
      if num[m] < num[m+1]:
        return self.findPeakElementRange(num, m+1, j)
      else:
        return self.findPeakElementRange(num, i, m)

if __name__ == '__main__':
  num = [1, 2]
  print Solution().findPeakElement(num)
