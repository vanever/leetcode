#include <iostream>
#include <algorithm>
#include <cassert>

using namespace std;

class Solution
{

public:

  int maxProduct(int A[], int n)
  {
    assert(n >= 1);

    int max, lastMax, lastMin, genByLastMax, genByLastMin;

    max = lastMax = A[0];
    lastMin = A[0];

    for (int i = 1; i < n; ++i)
    {
      lastMax *= A[i];  // may be max or min
      lastMin *= A[i];  // may be max or min

      genByLastMax = lastMax;
      genByLastMin = lastMin;

      // update last min negative
      lastMin = std::min(lastMin, A[i]);
      lastMin = std::min(lastMin, genByLastMax);

      // update last max positive
      lastMax = std::max(lastMax, A[i]);
      lastMax = std::max(genByLastMin, lastMax);

      // update max with production of positives
      max = std::max(lastMax, max);
    }
    return max;
  }

};

int main(int argc, char *argv[])
{
  int A[4] = { -2, 3, -4 };
  int B[4] = { -2, -1, -9, -6 };
  assert(Solution().maxProduct(A, 4) == 24);
  assert(Solution().maxProduct(B, 4) == 108);
  return 0;
}
