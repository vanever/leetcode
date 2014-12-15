# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  # @param head, a ListNode
  # @return a ListNode
  def insertionSortList(self, head):
    if head == None or head.next == None:
      return head
    nnext = head.next
    nhead = head
    head.next = None
    nLast = head
    while nnext != None:
      n = nhead
      prevn = None
      ncurr = nnext

      # optimize
      if nLast.val <= ncurr.val:
        nLast.next = ncurr
        nnext = ncurr.next
        nLast = ncurr
        nLast.next = None
        continue

      while n != None and ncurr.val > n.val :
        prevn = n
        n = n.next
      nnext = ncurr.next
      if n == None:
        assert prevn != None
        ncurr.next = None
        prevn.next = ncurr
        nLast = ncurr
      elif prevn == None:
        # insert from head
        nhead = ncurr
        nhead.next = n
      else:
        assert ncurr.val <= n.val
        prevn.next = ncurr
        ncurr.next = n
    return nhead

  def insertionSortList2(self, head):
    if head == None or head.next == None:
      return head

    setinel = ListNode(-1)
    setinel.next = head

    curr = head
    while curr.next != None:
      if curr.next.val < curr.val:
        n = setinel
        while n.next.val < curr.next.val:
          n = n.next
          assert n.next != None
        toInsert = curr.next
        curr.next = toInsert.next
        toInsert.next = n.next
        n.next = toInsert
      else:
        curr = curr.next
    return setinel.next


if __name__ == '__main__':
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)
  n6 = ListNode(6)

  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5
  n5.next = n6

  # n3.next = n4
  # n4.next = n1
  # n2.next = n5
  # n5.next = n3
  # n3.next = n6
  # n6.next = None

  s = Solution()

  head = s.insertionSortList2(n1)

  while head != None:
    print head.val
    head = head.next
