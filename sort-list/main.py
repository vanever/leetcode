# Definition for singly-linked list.
class ListNode:

  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:

  # @param head, a ListNode
  # @return a ListNode
  def sortList(self, head):
    """sort list in-place"""
    if head == None or head.next == None:
      return head

    numNode = 0
    n = head
    while n != None:
      n = n.next
      numNode += 1

    i = 1
    while i < numNode:
      j = 0
      nnext = head
      nLastTail = None
      first = True
      while nnext != None:
        n = nnext
        (nhead, ntail) = self.merge(n, i)
        if first:
          head = nhead
          nLastTail = ntail
          first = False
        else:
          nLastTail.next = nhead
        if ntail != None:
          nnext = ntail.next
          nLastTail = ntail

      i *= 2
        
    return nhead

  # @return (head, tail)
  def merge(self, node, length):

    if node == None or length <= 0:
      return (node, node)
    n1 = node
    n2 = node
    i = 0
    head = node
    tail = None

    while i < length and n2 != None:
      i += 1
      tail = n2
      n2 = n2.next

    if n2 == None:
      return (node, tail)

    length2 = 0
    tmp = n2
    while tmp and length2 < length:
      tmp = tmp.next
      length2 += 1

    # print "length1: %d, length2: %d" % (length, length2)
    # print "n1: %d, n2: %d" % (n1.val, n2.val)

    i1 = 0
    i2 = 0

    if n1.val < n2.val:
      head = n1
      n1 = n1.next
      i1 += 1
    else:
      head = n2
      n2 = n2.next
      i2 += 1

    ncurr = head
    tail  = head

    while i1 != length and i2 != length2:
      if n1.val < n2.val:
        ncurr.next = n1
        n1 = n1.next
        i1 += 1
      else:
        ncurr.next = n2
        n2 = n2.next
        i2 += 1

      ncurr = ncurr.next

    tail = ncurr

    if i1 == length:
      while i2 != length2:
        ncurr.next = n2
        n2 = n2.next
        ncurr = ncurr.next
        i2 += 1

    if i2 == length2:
      while i1 != length:
        ncurr.next = n1
        n1 = n1.next
        ncurr = ncurr.next
        i1 += 1

    tail = ncurr
    tail.next = n2

    #print ""

    # print 'debug: i == %d' % length
    # tmp = head
    # while tmp != tail:
    #   print tmp.val
    #   tmp = tmp.next
    # print tail.val

    return (head, tail)

if __name__ == '__main__':
  n1 = ListNode(1)
  n2 = ListNode(2)
  n3 = ListNode(3)
  n4 = ListNode(4)
  n5 = ListNode(5)
  n6 = ListNode(6)

  n3.next = n4
  n4.next = n1
  # n2.next = n5
  # n5.next = n3
  # n3.next = n6
  # n6.next = None

  s = Solution()

  head = s.sortList(n3)

  while head != None:
    print head.val
    head = head.next
