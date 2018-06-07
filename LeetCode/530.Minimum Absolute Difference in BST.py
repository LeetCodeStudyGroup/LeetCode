# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import sys
        self.diff = sys.maxint
        self.cur = None
        self.inorder(root)

        return self.diff

    def inorder(self, root):
        if root == None:
            return

        self.inorder(root.left)
        if self.cur:
            self.diff = min(self.diff, root.val - self.cur.val)
        self.cur = root
        self.inorder(root.right)
