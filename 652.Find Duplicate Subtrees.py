# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        from collections import defaultdict
        self.rst = []
        self.mem = defaultdict(int)
        self.postorder(root)
        return self.rst

    def postorder(self, node):
        if node == None:
            return '#'

        string = str(node.val) + "," + self.postorder(node.left) + "," + self.postorder(node.right)
        if self.mem[string] == 1:
            self.rst.append(node)
        self.mem[string] += 1
        return string
