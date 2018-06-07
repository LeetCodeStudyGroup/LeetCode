# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lstack = [root]
        rstack = [root]
        while len(lstack) > 0 and len(lstack) > 0:
            lnode = lstack.pop()
            rnode = rstack.pop()
            if lnode.val == rnode.val:
                if lnode.right and rnode.left:
                    lstack.append(lnode.right)
                    rstack.append(rnode.left)
                elif lnode.right or rnode.left:
                    return False
                if lnode.left and rnode.right:
                    lstack.append(lnode.left)
                    rstack.append(rnode.right)
                elif lnode.left or rnode.right:
                    return False
            else:
                return False
        return True
        #return self.symmetric(root, root)
        
    def symmetric(self, lnode, rnode):
        if not lnode and not rnode:
            return True
        elif (not lnode and rnode) or (lnode and not rnode):
            return False
        elif lnode and rnode and lnode.val != rnode.val:
            return False
        return self.symmetric(lnode.left, rnode.right) and self.symmetric(lnode.right, rnode.left)
