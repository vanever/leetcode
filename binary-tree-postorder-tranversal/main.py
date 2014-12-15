class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:

  # @param root, a tree node
  # @return a list of integers
  def postorderTraversal(self, root):

    rightHandled = dict()
    stack = list()
    out = []

    if root:
      stack.append(root)
      while root.left:
        stack.append(root.left)
        root = root.left

    while len(stack) > 0:
      node = stack[-1]
      if node in rightHandled:
        stack.pop()
        out.append(node.val)
        continue
      else:
        rightHandled[node] = 1
        if node.right:
          node = node.right
          stack.append(node)
          while node.left:
            node = node.left
            stack.append(node)
    return out


if __name__ == '__main__':
  s = Solution()
  root  = TreeNode(1)
  n2  = TreeNode(2)
  n3  = TreeNode(3)
  root.left = n2
  n2.right = n3
  ret = s.postorderTraversal(root)
  print ret
