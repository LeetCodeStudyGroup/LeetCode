# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.check(p, q)
        
    def check(self, p, q):
        if self.check_l_r(p, q):
            return False
        ret = True
        if p:
            if (p.val != q.val) or \
                self.check_l_r(p.left, q.left) or \
                self.check_l_r(p.right, q.right):
                return False
            if p.left:
                ret = ret and self.check(p.left, q.left)
            if p.right:
                ret = ret and self.check(p.right, q.right)
        return ret

    def check_l_r(self, p, q):
        return (not p and q) or (p and not q)
