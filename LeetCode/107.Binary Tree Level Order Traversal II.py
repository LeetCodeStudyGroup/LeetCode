# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.level_node(result, root, 0)
        return result
        
    def level_node(self, result, node, level):
        if node == None:
            return
        if level == len(result):
            result.insert(0, [])
        result[len(result) - 1 - level].append(node.val)
        self.level_node(result, node.left, level + 1)
        self.level_node(result, node.right, level + 1)
