# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []

        self.leaves = [root.val]
        self.get_left_bound(root.left)
        self.get_leaves(root.left)
        self.get_leaves(root.right)
        self.get_right_bound(root.right)

        return self.leaves

    def get_left_bound(self, node):
        if node == None:
            return
        if node.left:
            self.leaves.append(node.val)
            self.get_left_bound(node.left)
        elif node.right:
            self.leaves.append(node.val)
            self.get_left_bound(node.right)

    def get_right_bound(self, node):
        if node == None:
            return
        if node.right:
            self.get_right_bound(node.right)
            self.leaves.append(node.val)
        elif node.left:
            self.get_right_bound(node.left)
            self.leaves.append(node.val)

    def get_leaves(self, node):
        if node == None:
            return
        if node.left == None and node.right == None:
            self.leaves.append(node.val)
            return
        if node.left:
            self.get_leaves(node.left)
        if node.right:
            self.get_leaves(node.right)
