# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root, None, None)

    def check(self, node, min_val, max_val):
        if not node:
            return True
        elif (min_val != None and node.val <= min_val) or (max_val != None and node.val >= max_val):
            return False
        else:
            return self.check(node.left, min_val, node.val) and self.check(node.right, node.val, max_val)
