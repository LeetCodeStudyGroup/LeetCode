# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.rst = 0
        if root:
            self.helper(root, 0)
        return self.rst

    def helper(self, node, val):
        left_cnt, right_cnt = 0, 0
        if node.left:
            left_cnt = self.helper(node.left, node.val)
        if node.right:
            right_cnt = self.helper(node.right, node.val)
        self.rst = max(self.rst, left_cnt + right_cnt)
        if node.val != val:
            return 0
        return max(left_cnt, right_cnt) + 1
