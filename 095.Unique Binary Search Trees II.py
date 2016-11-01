# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.create_node(0, n -1)

    def create_tree(self, val, lstart, lend, rstart, rend):
        nodes = []
        for lnode in self.create_node(lstart, lend):
            for rnode in self.create_node(rstart, rend):
                root = TreeNode(val + 1)
                root.left = lnode
                root.right = rnode
                nodes.append(root)
        return nodes

    def create_node(self, start, end):
        nodes = []
        if (end - start) == 0:
            nodes.append(TreeNode(start + 1))
        elif (end - start) < 0:
            nodes.append(None)
        else:
            for i in range(start, end + 1):
                nodes.extend(self.create_tree(i, start, i - 1, i + 1, end))
        return nodes

    def copy_tree(self, node):
        if not node:
            return None
        new_node = TreeNode(node.val)
        new_node.left = self.copy_tree(node.left)
        new_node.right = self.copy_tree(node.right)
        return new_node
