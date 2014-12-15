# Definition for singly-linked list.

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @return nothing
  def reorderList(self, head):
    length = 0
    if head == None or head.next == None or head.next.next == None:
      return

    node = head
    while node:
      length += 1
      node = node.next
    halfLen = (length + 1) / 2

    node = head
    i = 1
    while i < halfLen:
      node = node.next
      i += 1
    rhead = node.next
    node.next = None
    rhead = self.reverseList(rhead)
    setinel = ListNode(0)
    newhead = setinel
    i = 0
    h1 = head
    h2 = rhead
    while i < length and h2:
      newhead.next = h1
      h1 = h1.next
      newhead.next.next = h2
      h2 = h2.next
      newhead = newhead.next.next
      i += 2

    if h1:
      newhead.next = h1

    return setinel.next

  def reverseList(self, head):
    prev = None
    while head.next:
      next = head.next
      head.next = prev
      prev = head
      head = next

    head.next = prev
    return head

if __name__ == '__main__':
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)
  n6 = ListNode(6)
  n7 = ListNode(7)

  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5
  n5.next = n6
  n6.next = n7

  Solution().reorderList(n1)

  while n1:
    print n1.val,
    n1 = n1.next
  print ""
