# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = collections.deque()
        queue.append(root)
        first_node = root
        while len(queue) > 0:
            size = len(queue)
            first_node = None
            for i in range(size):
                node = queue.popleft()
                if not first_node:
                    first_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return first_node.val
