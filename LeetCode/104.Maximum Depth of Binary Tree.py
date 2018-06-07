# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.trace(root, 0)
        
    def trace(self, node, num):
        if node == None:
            return num
        return max(self.trace(node.left, num + 1), self.trace(node.right, num + 1))
