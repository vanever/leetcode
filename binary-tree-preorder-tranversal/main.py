class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:

  # @param root, a tree node
  # @return a list of integers
  def preorderTraversal(self, root):
    stack = list()
    out = list()

    if root:
      stack.append(root)

    while len(stack) > 0:
      node = stack.pop()
      out.append(node.val)
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)
    return out


if __name__ == '__main__':
  s = Solution()
  root  = TreeNode(1)
  n2  = TreeNode(2)
  n3  = TreeNode(3)
  root.right = n2
  n2.right = n3
  ret = s.preorderTraversal(root)
  print ret
