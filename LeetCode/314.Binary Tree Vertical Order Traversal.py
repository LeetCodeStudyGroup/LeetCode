# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        if root == None:
            return rst

        from collections import deque
        from collections import defaultdict
        mapping = defaultdict(list)
        q = deque([(root, 0)])
        min_val, max_val = 0, 0
        while len(q) > 0:
            for _ in range(len(q)):
                node, col = q.popleft()
                mapping[col].append(node.val)
                if node.left:
                    q.append((node.left, col - 1))
                    min_val = min(min_val, col - 1)
                if node.right:
                    q.append((node.right, col + 1))
                    max_val = max(max_val, col + 1)
        for i in range(min_val, max_val + 1):
            rst.append(mapping[i])
        return rst
