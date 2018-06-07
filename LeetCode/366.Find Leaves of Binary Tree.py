# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.rst = []
        if root:
            self.rst.append([])
            self.helper(root)
        return self.rst

    def helper(self, node):
        if not node.left and not node.right:
            self.rst[0].append(node.val)
            return 1

        depth = 0
        if node.left:
            depth = self.helper(node.left)
        if node.right:
            depth = max(depth, self.helper(node.right))
        while len(self.rst) <= depth:
            self.rst.append([])
        self.rst[depth].append(node.val)
        return depth + 1
