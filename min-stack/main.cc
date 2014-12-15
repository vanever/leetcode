#include <vector>
#include <map>
#include <cassert>
#include <stack>

class MinStack
{

public:

  MinStack() {}

  void push(int x)
  {
    elements_.push(x);

    if (mins_.empty())
    {
      mins_.push(std::make_pair(x, 1));
    }
    else if (mins_.top().first == x)
    {
      mins_.top().second++;
    }
    else if (mins_.top().first > x)
    {
      mins_.push(std::make_pair(x, 1));
    }
  }

  void pop()
  {
    if (!elements_.empty())
    {
      if (mins_.top().first == elements_.top() && --mins_.top().second == 0)
      {
        mins_.pop();
      }
      elements_.pop();
    }
  }

  int top()
  {
    return elements_.top();
  }

  int getMin()
  {
    if (!mins_.empty())
    {
      return mins_.top().first;
    }
    else
    {
      throw std::runtime_error("stack is empty");
    }
  }

private:

  std::stack<int> elements_;
  std::stack<std::pair<int, int> > mins_;

};

int main(int argc, char *argv[])
{
  MinStack minStack;
  minStack.push(-2);
  minStack.push(0);
  minStack.push(-1);

  assert(minStack.getMin() == -2);
  assert(minStack.top() == -1);
  minStack.pop();
  assert(minStack.getMin() == -2);

  return 0;
}
