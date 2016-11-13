# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.modify(root, 0)
        return self.msearch(root, k)

    def msearch(self, node, k):
        if k == node.count:
            return node.val
        elif k < node.count:
            return self.msearch(node.left, k)
        else:
            return self.msearch(node.right, k)

    def modify(self, node, k):
        left_count = right_count = 0
        if node.left:
            left_count = self.modify(node.left, k)
        node.count = left_count + 1 + k
        if node.right:
            right_count = self.modify(node.right, node.count)
        return left_count + right_count + 1

    def kthSmallest2(self, root, k):
        return self.search(root, k)[1]

    def search(self, node, k):
        val = None
        if node.left:
            k, val = self.search(node.left, k)
        if k == 1:
            return 0, node.val
        k -= 1
        if node.right and val == None:
            k, val = self.search(node.right, k)
        return k, val
