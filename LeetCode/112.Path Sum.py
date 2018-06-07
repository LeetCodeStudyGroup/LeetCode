# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.check(root, sum, 0)

    def sum(self, node, target, cur):
        cur += node.val
        if node.left or node.right:
            return self.check(node.left, target, cur) or self.check(node.right, target, cur)
        else:
            return target == cur

    def check(self, node, target, cur):
        return node != None and self.sum(node, target, cur)
