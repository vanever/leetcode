#include <iostream>

using namespace std;

struct ListNode
{
  int val;
  ListNode * next;
  ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:

  ListNode * getIntersecionNode(ListNode * headA, ListNode * headB)
  {
    if (headA == NULL || headB == NULL)
    {
      return NULL;
    }

    ListNode * tailA = headA;
    ListNode * tailB = headB;
    ListNode * commonTail = NULL;

    while (tailA->next)
      tailA = tailA->next;
    while (tailB->next)
      tailB = tailB->next;

    if (tailA != tailB)
    {
      return NULL;
    }
    else
    {
      commonTail = tailA;
    }

    // make a ring
    commonTail->next = headA;

    tailA = headB->next;
    tailB = headB->next->next;

    // 2N = BeforeRingLength + Ring.Offset + Ring.Length
    //  N = BeforeRingLength + Ring.Offset
    while (tailA != tailB)
    {
      tailA = tailA->next;
      tailB = tailB->next->next;
    }

    // now we get tailA = tailB = Ring.Offset = N - BeforeRingLength
    // tailB is "BeforeRingLength" steps futher from intersected node
    // headB is also "BeforeRingLength" steps futher from intersected node
    // forward until these two nodes collide

    tailA = headB;
    while (tailA != tailB)
    {
      tailA = tailA->next;
      tailB = tailB->next;
    }

    // reset tail
    commonTail->next = 0;

    return tailA;
  }

};

int main(int argc, char *argv[])
{
  ListNode * node1 = new ListNode(1);
  ListNode * node2 = new ListNode(2);
  ListNode * node3 = new ListNode(3);
  ListNode * node4 = new ListNode(4);
  ListNode * node5 = new ListNode(5);
  ListNode * node6 = new ListNode(6);
  ListNode * node7 = new ListNode(7);

  node1->next = node2;
  node2->next = node3;
  node3->next = node4;
  node4->next = node5;
  node6->next = node7;
  node7->next = node2;

  ListNode * intersectedNode = Solution().getIntersecionNode(node1, node6);

  if (intersectedNode)
    cout << "intersected node value is " << intersectedNode->val << endl;
  else
    cout << "no intersected node" << endl;

  return 0;
}
