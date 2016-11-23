class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.do_rob(nums, 0, len(nums) - 1), self.do_rob(nums, 1, len(nums)))

    def do_rob(self, nums, start, size):
        include = exclude = 0
        for i in range(start, size):
            inc, exc = include, exclude
            include, exclude = exclude + nums[i], max(inc, exc)
        return max(include, exclude)

    def rob2(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        dp2[0], dp2[1] = 0, nums[1]
        for i in range(2, len(nums)):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp1[-2], dp2[-1])
