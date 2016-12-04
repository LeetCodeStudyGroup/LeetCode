class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        max_inx, max_cnt = -1, 0
        dp = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            index, count = i, 0
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0 and dp[j][1] > count:
                    index, count = j, dp[j][1]
            dp[i] = index, count + 1
            if dp[i][1] > max_cnt:
                max_inx, max_cnt = i, dp[i][1]
        rst = [nums[max_inx]]
        while max_inx != dp[max_inx][0]:
            rst.append(nums[dp[max_inx][0]])
            max_inx = dp[max_inx][0]
        return rst
