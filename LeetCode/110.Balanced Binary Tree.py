# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.get_depth(root, 0)[0]
        
    def get_depth(self, node, cnt):
        if node == None:
            return True, cnt
        ret1, depth1 = self.get_depth(node.left, cnt + 1)
        ret2, depth2 = self.get_depth(node.right, cnt + 1)
        ret = ret1 and ret2 and abs(depth1 - depth2) <= 1
        return ret, max(depth1, depth2)
