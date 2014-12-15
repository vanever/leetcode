# Definition for a undirected graph node
class UndirectedGraphNode:
  def __init__(self, x):
    self.label = x
    self.neighbors = []

class Solution:
  # @param node, a undirected graph node
  # @return a undirected graph node
  def cloneGraph(self, node):
    if node == None:
      return node
    stack = []
    stack.append(node)
    nodeDict = {}
    handledNode = set([])
    head = None
    while len(stack) > 0:

      node = stack.pop()
      if node.label in handledNode:
        continue

      if node.label in nodeDict:
        cnode = nodeDict[node.label]
      else:
        cnode = UndirectedGraphNode(node.label)
        nodeDict[node.label] = cnode
      if head == None:
        head = cnode

      for nb in node.neighbors:
        if nb.label in nodeDict:
          cnb = nodeDict[nb.label]
        else:
          cnb = UndirectedGraphNode(nb.label)
          nodeDict[nb.label] = cnb
        cnode.neighbors.append(cnb)
        if nb.label not in handledNode:
          stack.append(nb)

      handledNode.add(node.label)
    return head

  def printGraph(self, node):
    stack = []
    stack.append(node)
    handled = set()
    while len(stack) > 0:
      node = stack.pop()
      if node not in handled:
        print node.label,
        handled.add(node)
      else:
        continue
      for n in node.neighbors:
        print n.label,
        stack.append(n)
      print '#, '
    print ''

if __name__ == '__main__':
  n0 = UndirectedGraphNode(0)
  n1 = UndirectedGraphNode(1)
  n2 = UndirectedGraphNode(2)
  n0.neighbors.append(n1)
  n0.neighbors.append(n2)
  n1.neighbors.append(n2)
  n2.neighbors.append(n2)
  s = Solution()
  new = s.cloneGraph(n0)
  s.printGraph(n0)
  s.printGraph(new)
