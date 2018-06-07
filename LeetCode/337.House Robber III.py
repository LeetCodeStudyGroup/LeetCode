# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memory = {}
        return self.dfs(root, memory) if root else 0

    def dfs(self, root, memory):
        if root in memory:
            return memory[root]
        do_it = root.val
        not_do_it = 0
        if root.left:
            not_do_it += self.dfs(root.left, memory)
            if root.left.left:
                do_it += self.dfs(root.left.left, memory)
            if root.left.right:
                do_it += self.dfs(root.left.right, memory)
        if root.right:
            not_do_it += self.dfs(root.right, memory)
            if root.right.left:
                do_it += self.dfs(root.right.left, memory)
            if root.right.right:
                do_it += self.dfs(root.right.right, memory)
        memory[root] = max(do_it, not_do_it)
        return memory[root]
