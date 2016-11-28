class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.root = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start > end:
            return None
        root = SegTreeNode(start, end)
        if start == end:
            root.sum = nums[start]
        else:
            mid = (start + end) / 2
            root.left = self.build_tree(nums, start, mid)
            root.right = self.build_tree(nums, mid + 1, end)
            root.sum = root.left.sum + root.right.sum
        return root

    def get_sum(self, root, i, j):
        if root.start == i and root.end == j:
            return root.sum
        elif root.left.start <= i and root.left.end >= j:
            return self.get_sum(root.left, i, j)
        elif root.right.start <= i and root.right.end >= j:
            return self.get_sum(root.right, i, j)
        else:
            return self.get_sum(root.left, i, root.left.end) + self.get_sum(root.right, root.right.start, j)

    def update_heap(self, root, i, diff):
        root.sum += diff
        if root.start == root.end:
            return
        elif root.left.start <= i and root.left.end >= i:
            return self.update_heap(root.left, i, diff)
        elif root.right.start <= i and root.right.end >= i:
            return self.update_heap(root.right, i, diff)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        self.update_heap(self.root, i, diff)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_sum(self.root, i, j)

class SegTreeNode:
    def __init__(self, start, end):
        self.start, self.end, self.sum = start, end, 0
        self.left = self.right = None


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
