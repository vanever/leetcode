# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  # @param root, a tree node
  # @return an integer
  def sumNumbers(self, root):
    if root == None:
      return 0
    xsum = 0
    stack = []
    stack.append(root)
    parents = {}
    parents[root] = 0
    num = 0
    while len(stack) > 0:
      node = stack.pop()
      num = parents[node] * 10 + node.val
      if node.left == None and node.right == None:
        xsum += num
      else:
        if node.left:
          stack.append(node.left)
          parents[node.left] = num
        if node.right:
          stack.append(node.right)
          parents[node.right] = num
    return xsum


if __name__ == '__main__':
  s = Solution()
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3)
  n1.left = n2
  n1.right = n3
  print s.sumNumbers(n1)
  n1.left = n2
  n1.right = None
  n2.right = n3
  print s.sumNumbers(n1)
