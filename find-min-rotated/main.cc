#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

class Solution
{

public:

  int findMin(vector<int> & arr)
  {
    return findMinRange(arr, 0, arr.size() - 1);
  }

  int findMinRange(vector<int> arr, size_t l, size_t r)
  {
    if (arr.size() == 0 || l > r)
    {
      return -1;
    }

    while (arr[l] >= arr[r] && r - l > 1)
    {
      size_t m = l + (r - l) / 2;
      if (arr[m] > arr[l])
      {
        // min value must in [m+1, r]
        l = m + 1;
        assert(l <= r);
      }
      else if (arr[m] < arr[l])
      {
        // min value must in [l, m-1]
        r = m;
      }
      else
      {
        if (arr[r] == arr[m])
        {
          // worst condition
          assert((m+1) <= r);
          int minRight = findMinRange(arr, m+1, r);
          if (minRight < arr[m])
          {
            return minRight;
          }
          else
          {
            assert(l <= r);
            r = m - 1;
          }
        }
        else
        {
          assert(arr[m] > arr[r]);
          l = m + 1;
        }
      }
    }

    if (r - l > 1)
    {
      return arr[l];
    }
    else 
    {
      switch (r - l)
      {
      case 0:
        return arr[l];
        break;
      case 1:
        return arr[l] > arr[r] ? arr[r] : arr[l];
        break;
      default:
        break;
      }
    }

    return -1;
  }

};

int main(int argc, char *argv[])
{
  vector<int> arr;
  arr.push_back(3);
  arr.push_back(3);
  arr.push_back(1);

  assert(Solution().findMin(arr) == 1);

  return 0;
}
