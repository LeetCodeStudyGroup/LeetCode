# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root:
            self.do_flatten(root)
        
    def do_flatten(self, node):
        if node.left and node.right:
            llast = self.do_flatten(node.left)
            rlast = self.do_flatten(node.right)
            node.right, node.left, llast.right = node.left, None, node.right
            return rlast
        elif node.left:
            last = self.do_flatten(node.left)
            node.right, node.left = node.left, None
            return last
        elif node.right:
            return self.do_flatten(node.right)
        else:
            return node
