class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.record = []
        val = 0
        for i in range(len(nums)):
            val += nums[i]
            self.record.append(val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        r = self.record[j]
        if i != 0:
            r -= self.record[i - 1]
        return r

class Node:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.sum = sum

class NumArray2(object):
    def __init__(self, nums):
        size = 1
        while size < len(nums):
            size *= 2
        heap = [None] * size
        i = size - 1
        for inx in range(i, i / 2, -1):
            l, r = inx * 2 - size, inx * 2 + 1 - size
            if r < len(nums):
                heap[inx] = Node(l, r, nums[l] + nums[r])
            elif l < len(nums):
                heap[inx] = Node(l, l, nums[l])
        i /= 2
        while i > 0:
            for inx in range(i, i / 2, -1):
                l, r = inx * 2, inx * 2 + 1
                if heap[l] and heap[r]:
                    heap[inx] = Node(heap[l].start, heap[r].end, heap[l].sum + heap[r].sum)
                elif heap[l]:
                    heap[inx] = heap[l]
            i /= 2
        self.nums = nums
        self.heap = heap

    def get_sum(self, root, i, j):
        if i > j: return 0
        elif i == j:
            return self.nums[i]
        elif self.heap[root].start == i and self.heap[root].end == j:
            return self.heap[root].sum

        left, right = root * 2, root * 2 + 1
        if self.heap[left].start <= i and self.heap[left].end >= j:
            return self.get_sum(left, i, j)
        elif self.heap[right].start <= i and self.heap[right].end >= j:
            return self.get_sum(right, i, j)
        else:
            return self.get_sum(left, i, self.heap[left].end) + self.get_sum(right, self.heap[right].start, j)

    def sumRange(self, i, j):
        return self.get_sum(1, i, j)

class NumArray_TLE(object):
    def __init__(self, nums):
        self.size = len(nums)
        self.record = [0] * (len(nums) * (len(nums) + 1) / 2)
        for i in range(len(nums)):
            self.record[self.index(i, i)] = nums[i]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                self.record[self.index(i, j)] = self.record[self.index(i, j - 1)] + nums[j]

    def index(self, i, j):
        return (self.size * 2 - i + 1) * (i) / 2 + j - i

    def sumRange(self, i, j):
        return self.record[self.index(i, j)]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
