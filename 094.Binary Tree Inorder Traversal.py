# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.traversal(result, root)
        return result
        
    def traversal(self, result, node):
        if not node:
            return
        self.traversal(result, node.left)
        result.append(node.val)
        self.traversal(result, node.right)
