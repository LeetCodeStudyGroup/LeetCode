# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.do_sum(0, root)
        
    def do_sum(self, val, node):
        if node == None:
            return val
        val *= 10
        val += node.val
        if node.left and node.right:
            return self.do_sum(val, node.left) + self.do_sum(val, node.right)
        elif node.left:
            return self.do_sum(val, node.left)
        else:
            return self.do_sum(val, node.right)
