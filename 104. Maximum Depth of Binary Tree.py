# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 回傳 以 root 為節點的樹的高度
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_subtree_depth = 0
        right_subtree_depth = 0
        if root.left is not None:
            left_subtree_depth = self.maxDepth(root.left)

        if root.right is not None:
            right_subtree_depth = self.maxDepth(root.right)

        return 1 + max(left_subtree_depth, right_subtree_depth)
