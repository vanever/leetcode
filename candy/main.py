class Solution:
  # @param ratings, a list of integer
  # @return an integer
  def candy(self, ratings):

    size = len(ratings)
    if size <= 1:
      return size

    numCandy = 1
    prev_candy = 1
    curr_candy = 1

    peak = 0
    peakv1 = 1
    peakv2 = 0
    increased = False

    for i in range(1, size):
      if ratings[i] > ratings[i-1] or (ratings[i] == ratings[i-1]):
        curr_candy = prev_candy + 1 if ratings[i] > ratings[i-1] else 1
        numCandy += curr_candy
        prev_candy = curr_candy
        peak = i
        peakv1 = curr_candy
        peakv2 = 0
        increased = True
      else:
        if prev_candy != 1:
          curr_candy = 1
          numCandy += 1
        else:
          # we met some trouble
          # range(peak+1, i) must add 1
          assert i > peak
          numCandy += i - peak
          peakv2 += 1
          curr_candy = 1

          assert peakv2 <= peakv1

          if peakv2 == peakv1:
            peakv1 += 1
            numCandy += 1

        if increased:
          peakv2 = curr_candy
          increased = False

        prev_candy = curr_candy

    return numCandy

if __name__ == '__main__':
  s= Solution()
  ratings = [1, 2, 3, 4, 5]
  print s.candy(ratings)
  assert s.candy(ratings) == sum(ratings)
  ratings = [1, 2, 3, 2, 1]
  print s.candy(ratings)
  assert s.candy(ratings) == sum(ratings)
  ratings = [1, 2, 2, 2, 1]
  print s.candy(ratings)
  assert s.candy(ratings) == 7
  ratings = [0]
  print s.candy(ratings)
  assert s.candy(ratings) == 1
  ratings = [1, 2, 2, 1]
  print s.candy(ratings)
  assert s.candy(ratings) == sum(ratings)
  ratings = [1, 3, 2, 1]
  print s.candy(ratings)
  assert s.candy(ratings) == sum(ratings)
  ratings = [1, 0, 2]
  print s.candy(ratings)
  assert s.candy(ratings) == 5
