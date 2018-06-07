# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closest = root.val
        self.iterative(root, target)
        #self.recursive(root, target)
        return self.closest
    
    def iterative(self, root, target):
        while root != None:
            if abs(root.val - target) < abs(self.closest - target):
                self.closest = root.val
            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                root = None

    def recursive(self, node, target):
        if node == None:
            return

        if abs(node.val - target) < abs(self.closest - target):
            self.closest = node.val

        if node.val > target:
            if node.left:
                self.helper(node.left, target)
        elif node.val < target:
            if node.right:
                self.helper(node.right, target)
