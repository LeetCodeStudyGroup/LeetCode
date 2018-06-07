# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root

    def invert(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
