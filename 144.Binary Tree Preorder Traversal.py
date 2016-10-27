# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.preorder(result, root)
        return result
    
    def preorder(self, result, node):
        if not node:
            return
        result.append(node.val)
        self.preorder(result, node.left)
        self.preorder(result, node.right)
