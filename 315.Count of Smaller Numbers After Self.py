class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = [0] * len(nums)
        root = None
        for i in range(len(nums) - 1, -1, -1):
            root = self.insert(nums[i], root, rst, i, 0)
        return rst

    def insert(self, num, node, rst, i, presum):
        if node == None:
            node = Node(num, 0)
            rst[i] = presum
        elif node.num == num:
            node.dup += 1
            rst[i] = presum + node.count
        elif node.num > num:
            node.count += 1
            node.left = self.insert(num, node.left, rst, i, presum)
        else:
            node.right = self.insert(num, node.right, rst, i, presum + node.dup + node.count)
        return node

class Node(object):
    def __init__(self, n, c):
        self.num = n
        self.count = c
        self.dup = 1
        self.left = None
        self.right = None
