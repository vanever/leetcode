#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <cassert>

using namespace std;

class Solution
{
public:
  int evalRPN(vector<string> & tokens)
  {
    stack<int> notationStack;
    for (vector<string>::iterator it = tokens.begin(); it != tokens.end(); ++it)
    {
      const string & token = *it;
      if (token == "+")
      {
        assert(notationStack.size() >= 2);
        int v1 = notationStack.top(); notationStack.pop();
        int v2 = notationStack.top(); notationStack.pop();
        notationStack.push(v2 + v1);
      }
      else if (token == "-")
      {
        assert(notationStack.size() >= 2);
        int v1 = notationStack.top(); notationStack.pop();
        int v2 = notationStack.top(); notationStack.pop();
        notationStack.push(v2 - v1);
      }
      else if (token == "*")
      {
        assert(notationStack.size() >= 2);
        int v1 = notationStack.top(); notationStack.pop();
        int v2 = notationStack.top(); notationStack.pop();
        notationStack.push(v2 * v1);
      }
      else if (token == "/")
      {
        assert(notationStack.size() >= 2);
        int v1 = notationStack.top(); notationStack.pop();
        int v2 = notationStack.top(); notationStack.pop();
        notationStack.push(v2 / v1);
      }
      else
      {
        int v = atoi(token.c_str());
        notationStack.push(v);
      }
    }

    assert (notationStack.size() == 1);

    return notationStack.top();
  }
};

int main(int argc, char *argv[])
{
  vector<string> tokens;

  tokens.push_back("2");
  tokens.push_back("1");
  tokens.push_back("+");
  tokens.push_back("3");
  tokens.push_back("*");

  int r = Solution().evalRPN(tokens);
  cout << r << endl;
  assert(r == 9);

  tokens.clear();
  tokens.push_back("4");
  tokens.push_back("13");
  tokens.push_back("5");
  tokens.push_back("/");
  tokens.push_back("+");

  r = Solution().evalRPN(tokens);
  cout << r << endl;
  assert(r == 6);

  return 0;
}

