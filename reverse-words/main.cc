#include <iostream>
#include <string>
#include <cassert>

using namespace std;

class Solution
{

public:

  void reverseWords(string & s)
  {

    enum State
    {
      BEGIN,
      NORMAL,
      MIDDLE_SPACE,
    };

    size_t size = s.size(), dest = 0, word_start = 0, word_end = 0;

    State state = BEGIN;

    // 1. normalize the string

    for (size_t i = 0; i < size; ++i)
    {
      if (!is_space(s[i]))
      {
        if (dest != i)
        {
          s[dest++] = s[i];
        }
        else
        {
          dest++;
        }

        switch (state)
        {
        case BEGIN:
          word_start = dest - 1;
          break;
        case NORMAL:
          break;
        case MIDDLE_SPACE:
          word_start = dest - 1;
          break;
        default:
          assert(0);
          break;
        }

        state = NORMAL;
      }
      else
      {
        switch (state)
        {
        case BEGIN:
          continue;
          break;
        case NORMAL:
          s[dest++] = s[i];
          state = MIDDLE_SPACE;
          word_end = dest - 2;
          reverse(&s[0], word_start, word_end);
          break;
        case MIDDLE_SPACE:
          continue;
          break;
        default:
          assert(0);
          break;
        }
      }
    }

    // cut the tailing space
    if (is_space(s[dest - 1]))
    {
      dest--;
    }
    else if (state != BEGIN)
    {
      // reverse last word
      reverse(&s[0], word_start, dest - 1);
    }

    assert(dest > 0);

    s.resize(dest);

    // 2. reverse words
    reverse(&s[0], 0, dest - 1);
  }

  void reverse(char * arr, int l, int r)
  {
    if (l >= r)
    {
      return;
    }

    while (l < r)
    {
      swap(arr[l], arr[r]);
      l++;
      r--;
    }
  }

  bool is_space(char c) 
  {
    return c == ' ';
  }

};

int main(int argc, char *argv[])
{
  // std::string str = "   this is    the blue sky    ";
  std::string str = "a";
  Solution().reverseWords(str);
  cout << str << endl;
  return 0;
}
