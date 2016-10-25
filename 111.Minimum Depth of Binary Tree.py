# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.get_depth(root, 1)
        
    def get_depth(self, node, cnt):
        if node.left and node.right:
            return min(self.get_depth(node.left, cnt + 1), self.get_depth(node.right, cnt + 1))
        elif node.left:
            return self.get_depth(node.left, cnt + 1)
        elif node.right:
            return self.get_depth(node.right, cnt + 1)
        else:
            return cnt
