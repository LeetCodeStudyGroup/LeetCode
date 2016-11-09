# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        sets = []
        if root:
            self.create_path(sets, [], root)
        return sets

    def create_path(self, sets, ary, node):
        ary.append(str(node.val))
        if node.left and node.right:
            self.create_path(sets, ary[:], node.left)
            self.create_path(sets, ary, node.right)
        elif node.left:
            self.create_path(sets, ary, node.left)
        elif node.right:
            self.create_path(sets, ary, node.right)
        else:
            sets.append('->'.join(ary))
