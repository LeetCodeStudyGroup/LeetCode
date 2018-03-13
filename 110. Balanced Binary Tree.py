# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class ReturnType(object):
    is_balance = True
    max_depth = 0
    
    def __init__(self, is_balance, max_depth):
        self.is_balance = is_balance
        self.max_depth = max_depth
        

class Solution(object):
    
    def helper(self, root):
        if root is None:
            return ReturnType(True, 0)
        
        left_result = self.helper(root.left)
        right_result = self.helper(root.right)
        
        if left_result.is_balance == False or right_result.is_balance == False:
            return ReturnType(False, -1)
        
        if abs(left_result.max_depth - right_result.max_depth) > 1:
            return ReturnType(False, -1)
        
        return ReturnType(True, 1 + max(left_result.max_depth, right_result.max_depth))
        

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root).is_balance
        
