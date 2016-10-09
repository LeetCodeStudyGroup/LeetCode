# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        if root:
            self.sum(result, root, sum, [], 0)
        return result

    def sum(self, result, node, target, path, cur):
        cur += node.val
        path.append(node.val)
        if not node.left and not node.right and cur == target:
            result.append(path)
        elif node.left or node.right:
            if node.left:
                self.sum(result, node.left, target, path[:], cur)
            if node.right:
                self.sum(result, node.right, target, path, cur)
