# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        record = []
        if root:
            record.append(root)
        while len(record) > 0:
            cur = []
            for i in range(len(record)):
                node = record.pop(0)
                cur.append(node.val)
                if node.left:
                    record.append(node.left)
                if node.right:
                    record.append(node.right)
            result.append(cur)
        return result
