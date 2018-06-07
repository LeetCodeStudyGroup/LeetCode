class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        value = sum(nums)
        if value % 2 == 1:
            return False
        return self.checkTarget(nums, value / 2)

    def checkTarget(self, nums, target):
        dp = set([0])
        for num in nums:
            next_dp = set(dp)
            for key in dp:
                if key + num == target:
                    return True
                next_dp.add(key + num)
            dp = next_dp
        return False

    def checkTarget2(self, nums, target):
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, -1, -1):
                if i >= num:
                    dp[i] = dp[i] or dp[i - num]
        return dp[target]
