class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) == 0 or k > len(nums) or k == 0:
            return 0

        s = 0.0
        for i in range(k):
            s += nums[i]
        max_val = s
        for i in range(len(nums) - k):
                s = s - nums[i] + nums[i + k]
                max_val = max(max_val,  s)
        return max_val / k
