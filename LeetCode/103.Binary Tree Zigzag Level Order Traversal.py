# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        record = []
        if root:
            record.append(root)
        is_left = False
        while len(record) > 0:
            cur = []
            for i in range(len(record)):
                node = record.pop(0)
                cur.append(node.val)
                if node.left:
                    record.append(node.left)
                if node.right:
                    record.append(node.right)
            if is_left:
                cur.reverse()
            result.append(cur)
            is_left = not is_left
        return result
