class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        nums.sort()
        for i in range(target, -1, -1):
            dp[i] = self.get_count(dp, i, nums, target)
        return dp[0]

    def get_count(self, dp, i, nums, target):
        count = 0
        for num in nums:
            if i + num > target:
                break
            elif i + num == target:
                count += 1
            else:
                count += dp[i + num]
        return count
