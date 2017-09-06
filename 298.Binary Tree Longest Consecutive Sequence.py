# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        if root:
            self.counting(root)
        return self.count

    def counting(self, root):
        cnt = 0
        if root.left:
            l_cnt = self.counting(root.left)
            if root.val + 1 == root.left.val:
                cnt = max(cnt, l_cnt)
        if root.right:
            r_cnt = self.counting(root.right)
            if root.val + 1 == root.right.val:
                cnt = max(cnt, r_cnt)
        self.count = max(cnt + 1, self.count)
        return cnt + 1
