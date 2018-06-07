# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        from collections import defaultdict
        presum = defaultdict(int)
        presum[0] = 1
        self.count = 0
        self.helper(root, presum, 0, sum)
        return self.count

    def helper(self, node, presum, cursum, target):
        if node == None:
            return

        cursum += node.val
        self.count += presum[cursum - target]
        presum[cursum] += 1
        self.helper(node.left, presum, cursum, target)
        self.helper(node.right, presum, cursum, target)
        presum[cursum] -= 1

    def pathSum2(self, root, sum):
        self.count = 0
        if root:
            self.helper2(root, sum)
        return self.count

    def helper2(self, node, target):
        if node.val == target:
            self.count += 1

        new_lst = [node.val]
        if node.left:
            lst = self.helper2(node.left, target)
            for i in range(len(lst)):
                if lst[i] + node.val == target:
                    self.count += 1
                new_lst.append(lst[i] + node.val)
        if node.right:
            lst = self.helper2(node.right, target)
            for i in range(len(lst)):
                if lst[i] + node.val == target:
                    self.count += 1
                new_lst.append(lst[i] + node.val)
        return new_lst
