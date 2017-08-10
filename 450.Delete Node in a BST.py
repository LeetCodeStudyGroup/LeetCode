# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        return self.helper(None, root, key)

    def helper(self, parent, node, key):
        if node == None:
            return parent

        if node.val == key:
            new_node = node.left
            if new_node == None:
                new_node = node.right

            if node.left and node.right:
                tmp = node.left
                while tmp.right != None:
                    tmp = tmp.right
                tmp.right = node.right
            if parent:
                if parent.val > node.val:
                    parent.left = new_node
                else:
                    parent.right = new_node
                return parent
            else:
                return new_node
        elif node.val > key:
            self.helper(node, node.left, key)
        else:
            self.helper(node, node.right, key)

        return parent if parent else node
