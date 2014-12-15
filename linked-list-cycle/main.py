class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def hasCycle(self, head):
    if head == None or head.next == None:
      return False
    n1 = head.next
    n2 = head.next.next
    while n1 != n2 and n2 != None:
      n1 = n1.next
      n2 = n2.next
      if n2 == None:
        return False
      else:
        n2 = n2.next
    return True

if __name__ == '__main__':
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)

  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5
  n5.next = None

  print Solution().hasCycle(n1)
