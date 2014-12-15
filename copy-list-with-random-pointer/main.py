# Definition for singly-linked list with a random pointer.
class RandomListNode:
  def __init__(self, x):
    self.label = x
    self.next = None
    self.random = None

class Solution:
  # @param head, a RandomListNode
  # @return a RandomListNode
  def copyRandomList(self, head):
    if head == None:
      return None

    self.nodeDict = {}
    newhead = RandomListNode(head.label)
    self.nodeDict[head] = newhead

    h = head
    nh = newhead

    while head.next:
      newhead.next = RandomListNode(head.next.label)
      newhead = newhead.next
      head = head.next
      self.nodeDict[head] = newhead

    head = h
    while head:
      self.nodeDict[head].random = self.nodeDict[head.random] if head.random != None else None
      head = head.next
    return nh

if __name__ == '__main__':
  n1 = RandomListNode(1)
  n2 = RandomListNode(2)
  n3 = RandomListNode(3)
  n4 = RandomListNode(4)
  n5 = RandomListNode(5)

  n1.next = n2
  n2.next = n3
  n3.next = n4
  n4.next = n5
  n5.next = None
  n1.random = n4

  new = Solution().copyRandomList(n1)
  while new:
    print new.label,
    if new.random:
      print new.random.label,
    print ""
    new = new.next
