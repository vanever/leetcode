class Solution:
  # @param gas, a list of integers
  # @param cost, a list of integers
  # @return an integer
  def canCompleteCircuit(self, gas, cost):

    size = len(gas)

    if size == 0:
      return -1

    def next(n):
      return (n+1) % size

    diff = []
    for i in range(0, size):
      diff.append(gas[i] - cost[i])

    begin = 0
    i = 0
    gmax = diff[0]
    currMax = diff[0]
    currBegin = 0
    round = 0

    while next(i) != begin or round != 1:
      nexti = next(i)
      if nexti == begin:
        round = 1
      if diff[nexti] > currMax + diff[nexti]:
        currBegin = nexti
      currMax = max(diff[nexti], currMax + diff[nexti])
      if currMax > gmax:
        begin = currBegin 
        gmax = currMax
      i = nexti

    i = begin
    c = 0
    while True:
      c += gas[i] - cost[i]
      if c < 0:
        return -1
      if next(i) == begin:
        break
      i = next(i)

    return begin

if __name__ == '__main__':
  s = Solution()
  gas = [5, 5, 5, 5, 5]
  cost = [10, 1, 1, 2, 9]
  print s.canCompleteCircuit(gas, cost)
  assert s.canCompleteCircuit(gas, cost) == 1
  gas = [4]
  cost = [5]
  print s.canCompleteCircuit(gas, cost)
  assert s.canCompleteCircuit(gas, cost) == -1
  gas  = [4,5,6,7,8,9,1,2,3]
  cost = [2,3,4,5,6,7,8,9,1]
  print s.canCompleteCircuit(gas, cost)
  assert s.canCompleteCircuit(gas, cost) == 8
