# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.get_sum(root, False)

    def get_sum(self, node, is_left):
        if node.left and node.right:
            return self.get_sum(node.left, True) + self.get_sum(node.right, False)
        elif node.left:
            return self.get_sum(node.left, True)
        elif node.right:
            return self.get_sum(node.right, False)
        else:
            return node.val if is_left else 0
