# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @return a list node
  def detectCycle(self, head):
    if head == None or head.next == None:
      return None
    n1 = head.next
    n2 = head.next.next
    while n1 != n2 and n2 != None:
      n1 = n1.next
      n2 = n2.next
      if n2 == None:
        break
      else:
        n2 = n2.next
    if n2 == None:
      return None
    else:
      assert n1 == n2
      n = head
      while n != n1:
        n = n.next
        n1 = n1.next
      return n

if __name__ == '__main__':
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)
  n0 = ListNode(0)

  n0.next = n1
  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5
  n5.next = n1

  n = Solution().detectCycle(n0)
  print n.val

  n5.next = None
  n = Solution().detectCycle(n0)
  print n == None
