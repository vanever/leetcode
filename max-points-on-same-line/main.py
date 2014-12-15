class Point:
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

class MyPoint:
  def __init__(self, point):
    self.x = point.x
    self.y = point.y
  def __hash__(self):
    return self.x * 1017 + self.y * 73
  def __eq__(self, point):
    return self.x == point.x and self.y == point.y

class Solution:
  # @param points, a list of point
  # @return int
  def maxPoints(self, points):

    maxNum = 1
    numPoints = len(points)
    infinite = float("inf")

    pointsDict = dict()
    unifiedPoints = []

    if numPoints <= 1:
      return numPoints

    for p in points:
      mpoint = MyPoint(p)
      if not mpoint in pointsDict:
        pointsDict[mpoint] = 1
        unifiedPoints.append(mpoint)
      else:
        pointsDict[mpoint] += 1
      maxNum = max(pointsDict[mpoint], maxNum)

    numPoints = len(unifiedPoints)

    for i in range(0, numPoints):
      slopes = dict()
      for j in range(i + 1, numPoints):
        if unifiedPoints[i].x == unifiedPoints[j].x:
          slope = infinite
        else:
          slope = float(unifiedPoints[i].y - unifiedPoints[j].y) / float(unifiedPoints[i].x - unifiedPoints[j].x)
        if slope in slopes:
          slopes[slope] += pointsDict[unifiedPoints[j]]
        else:
          slopes[slope] = pointsDict[unifiedPoints[j]] + pointsDict[unifiedPoints[i]]
        maxNum = max(maxNum, slopes[slope])

    # print maxNum
    return maxNum


if __name__ == "__main__":
  # points = [(40,-23),(9,138),(429,115),(50,-17),(-3,80),(-10,33),(5,-21),(-3,80),(-6,-65),(-18,26),(-6,-65),(5,72),(0,77),(-9,86),(10,-2),(-8,85),(21,130),(18,-6),(-18,26),(-1,-15),(10,-2),(8,69),(-4,63),(0,3),(-4,40),(-7,84),(-8,7),(30,154),(16,-5),(6,90),(18,-6),(5,77),(-4,77),(7,-13),(-1,-45),(16,-5),(-9,86),(-16,11),(-7,84),(1,76),(3,77),(10,67),(1,-37),(-10,-81),(4,-11),(-20,13),(-10,77),(6,-17),(-27,2),(-10,-81),(10,-1),(-9,1),(-8,43),(2,2),(2,-21),(3,82),(8,-1),(10,-1),(-9,1),(-12,42),(16,-5),(-5,-61),(20,-7),(9,-35),(10,6),(12,106),(5,-21),(-5,82),(6,71),(-15,34),(-10,87),(-14,-12),(12,106),(-5,82),(-46,-45),(-4,63),(16,-5),(4,1),(-3,-53),(0,-17),(9,98),(-18,26),(-9,86),(2,77),(-2,-49),(1,76),(-3,-38),(-8,7),(-17,-37),(5,72),(10,-37),(-4,-57),(-3,-53),(3,74),(-3,-11),(-8,7),(1,88),(-12,42),(1,-37),(2,77),(-6,77),(5,72),(-4,-57),(-18,-33),(-12,42),(-9,86),(2,77),(-8,77),(-3,77),(9,-42),(16,41),(-29,-37),(0,-41),(-21,18),(-27,-34),(0,77),(3,74),(-7,-69),(-21,18),(27,146),(-20,13),(21,130),(-6,-65),(14,-4),(0,3),(9,-5),(6,-29),(-2,73),(-1,-15),(1,76),(-4,77),(6,-29)]
  points = []
  points.append(Point(2, 2))
  points.append(Point(0, 0))
  points.append(Point(0, 0))
  # points.append(Point(4, 5))
  # points.append(Point(40,-23))
  # points.append(Point(9,138))
  # points.append(Point(429,115))
  # points.append(Point(50,-17))
  # points.append(Point(-3,80))
  # points.append(Point(-10,33))
  # points.append(Point(5,-21))
  # points.append(Point(-3,80))
  # points.append(Point(-6,-65))
  # points.append(Point(-18,26))
  # points.append(Point(-6,-65))
  # points.append(Point(5,72))
  # points.append(Point(0,77))
  # points.append(Point(-9,86))
  # points.append(Point(10,-2))
  # points.append(Point(-8,85))
  # points.append(Point(21,130))
  # points.append(Point(18,-6))
  # points.append(Point(-18,26))
  # points.append(Point(-1,-15))
  # points.append(Point(10,-2))
  # points.append(Point(8,69))
  # points.append(Point(-4,63))
  # points.append(Point(0,3))
  # points.append(Point(-4,40))
  # points.append(Point(-7,84))
  # points.append(Point(-8,7))
  # points.append(Point(30,154))
  # points.append(Point(16,-5))
  # points.append(Point(6,90))
  # points.append(Point(18,-6))
  # points.append(Point(5,77))
  # points.append(Point(-4,77))
  # points.append(Point(7,-13))
  # points.append(Point(-1,-45))
  # points.append(Point(16,-5))
  # points.append(Point(-9,86))
  # points.append(Point(-16,11))
  # points.append(Point(-7,84))
  # points.append(Point(1,76))
  # points.append(Point(3,77))
  # points.append(Point(10,67))
  # points.append(Point(1,-37))
  # points.append(Point(-10,-81))
  # points.append(Point(4,-11))
  # points.append(Point(-20,13))
  # points.append(Point(-10,77))
  # points.append(Point(6,-17))
  # points.append(Point(-27,2))
  # points.append(Point(-10,-81))
  # points.append(Point(10,-1))
  # points.append(Point(-9,1))
  # points.append(Point(-8,43))
  # points.append(Point(2,2))
  # points.append(Point(2,-21))
  # points.append(Point(3,82))
  # points.append(Point(8,-1))
  # points.append(Point(10,-1))
  # points.append(Point(-9,1))
  # points.append(Point(-12,42))
  # points.append(Point(16,-5))
  # points.append(Point(-5,-61))
  # points.append(Point(20,-7))
  # points.append(Point(9,-35))
  # points.append(Point(10,6))
  # points.append(Point(12,106))
  # points.append(Point(5,-21))
  # points.append(Point(-5,82))
  # points.append(Point(6,71))
  # points.append(Point(-15,34))
  # points.append(Point(-10,87))
  # points.append(Point(-14,-12))
  # points.append(Point(12,106))
  # points.append(Point(-5,82))
  # points.append(Point(-46,-45))
  # points.append(Point(-4,63))
  # points.append(Point(16,-5))
  # points.append(Point(4,1))
  # points.append(Point(-3,-53))
  # points.append(Point(0,-17))
  # points.append(Point(9,98))
  # points.append(Point(-18,26))
  # points.append(Point(-9,86))
  # points.append(Point(2,77))
  # points.append(Point(-2,-49))
  # points.append(Point(1,76))
  # points.append(Point(-3,-38))
  # points.append(Point(-8,7))
  # points.append(Point(-17,-37))
  # points.append(Point(5,72))
  # points.append(Point(10,-37))
  # points.append(Point(-4,-57))
  # points.append(Point(-3,-53))
  # points.append(Point(3,74))
  # points.append(Point(-3,-11))
  # points.append(Point(-8,7))
  # points.append(Point(1,88))
  # points.append(Point(-12,42))
  # points.append(Point(1,-37))
  # points.append(Point(2,77))
  # points.append(Point(-6,77))
  # points.append(Point(5,72))
  # points.append(Point(-4,-57))
  # points.append(Point(-18,-33))
  # points.append(Point(-12,42))
  # points.append(Point(-9,86))
  # points.append(Point(2,77))
  # points.append(Point(-8,77))
  # points.append(Point(-3,77))
  # points.append(Point(9,-42))
  # points.append(Point(16,41))
  # points.append(Point(-29,-37))
  # points.append(Point(0,-41))
  # points.append(Point(-21,18))
  # points.append(Point(-27,-34))
  # points.append(Point(0,77))
  # points.append(Point(3,74))
  # points.append(Point(-7,-69))
  # points.append(Point(-21,18))
  # points.append(Point(27,146))
  # points.append(Point(-20,13))
  # points.append(Point(21,130))
  # points.append(Point(-6,-65))
  # points.append(Point(14,-4))
  # points.append(Point(0,3))
  # points.append(Point(9,-5))
  # points.append(Point(6,-29))
  # points.append(Point(-2,73))
  # points.append(Point(-1,-15))
  # points.append(Point(1,76))
  # points.append(Point(-4,77))
  # points.append(Point(1, 1))
  # points.append(Point(2, 2))
  # points.append(Point(2, 3))
  # points.append(Point(3, 4))
  # points.append(Point(4, 5))
  s = Solution()
  print s.maxPoints(points)
