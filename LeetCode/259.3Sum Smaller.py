class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        rst = 0
        nums.sort()
        for i, num in enumerate(nums):
            rst += self.twosum(nums, i + 1, len(nums) - 1, target - num)
        return rst

    def twosum(self, nums, start, end, target):
        rst = 0
        while start < end:
            if nums[start] + nums[end] < target:
                rst += end - start
                start += 1
            else:
                end -= 1
        return rst
