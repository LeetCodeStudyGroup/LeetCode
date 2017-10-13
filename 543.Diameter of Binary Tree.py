# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        if root:
            self.helper(root)
        return self.diameter - 1 if self.diameter > 0 else 0

    def helper(self, node):
        left, right = 0, 0
        if node.left:
            left = self.helper(node.left)
        if node.right:
            right = self.helper(node.right)
        self.diameter = max(self.diameter, left + right + 1)
        return max(left, right) + 1
