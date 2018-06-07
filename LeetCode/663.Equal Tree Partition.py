# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        from collections import defaultdict
        count = defaultdict(int)
        val = self.getsum(root, count)
        if val == 0:
            return count[0] > 1
        return val % 2 == 0 and val / 2 in count

    def getsum(self, node, count):
        if node == None:
            return 0
        val = node.val + self.getsum(node.left, count) + self.getsum(node.right, count)
        count[val] += 1
        return val

    def checkEqualTree2(self, root):
        if root == None:
            return False
        self.getsum2(root)
        return self.check_tree(root, 0)

    def check_tree(self, node, val):
        val += node.val
        if node.left and node.right:
            if val + node.right.sum == node.left.sum or val + node.left.sum == node.right.sum:
                return True
            return self.check(node.left, val) or self.check(node.right, val)
        elif node.left:
            if val == node.left.sum:
                return True
            return self.check(node.left, val)
        elif node.right:
            if val == node.right.sum:
                return True
            return self.check(node.right, val)
        return False

    def getsum2(self, node):
        node.sum = node.val
        if node.left:
            self.getsum(node.left)
            node.sum += node.left.sum
        if node.right:
            self.getsum(node.right)
            node.sum += node.right.sum
