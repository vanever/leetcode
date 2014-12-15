class Node:
  def __init__(self, v):
    self.v = v
    self.prev = self
    self.next = self

class LRUCache:

  # @param capacity, an integer
  def __init__(self, capacity):
    self.cap = capacity
    self.num = 0
    self.setinel = Node(0)
    self.dict = dict()

  # @return an integer
  def get(self, key):
    if key in self.dict:
      node = self.dict[key]
      self.touchNode(node)
      return node.v[1]
    else:
      return -1

  # readjust sequence
  def touchNode(self, node):
    if node != None:
      # delete from original pos 
      node.prev.next = node.next
      node.next.prev = node.prev
      # move to head
      t = self.setinel.next
      self.setinel.next = node
      node.prev = self.setinel
      t.prev = node
      node.next = t

  # insert a node in front of the list
  def insertHead(self, node):
    t = self.setinel.next
    self.setinel.next = node
    node.prev = self.setinel
    t.prev = node
    node.next = t
    # increment num
    self.num += 1
    # update dict
    if node.v[0] not in self.dict:
      self.dict[node.v[0]] = node

  # @param key, an integer
  # @param value, an integer
  # @return nothing
  def set(self, key, value):

    if key in self.dict:
      node = self.dict[key]
      node.v = (key, value)
      self.touchNode(node)
    else:
      node = Node((key, value))
      if self.num < self.cap:
        self.insertHead(node)
      else:
        # remove last one
        tail = self.setinel.prev
        tail.prev.next = tail.next
        tail.next.prev = tail.prev
        self.num -= 1
        self.insertHead(node)

        # update dict
        self.dict.pop(tail.v[0])

  def printme(self):
    head = self.setinel.next
    while head != self.setinel:
      print head.v[0],
      head = head.next
    print ""

if __name__ == '__main__':
  cache = LRUCache(3)
  cache.set(4, 0)
  cache.printme()
  cache.set(3, 0)
  cache.printme()
  cache.set(4, 0)
  cache.printme()
  cache.set(2, 0)
  cache.printme()
  cache.set(3, 0)
  cache.printme()
  cache.set(1, 0)
  cache.printme()
  cache.set(4, 0)
  cache.printme()
  cache.set(4, 0)
