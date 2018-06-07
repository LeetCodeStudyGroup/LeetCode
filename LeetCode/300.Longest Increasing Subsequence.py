class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val, length = 0, [0] * len(nums)
        for num in nums:
            start, end = 0, max_val
            while start != end:
                mid = (start + end) / 2
                if length[mid] < num:
                    start = mid + 1
                else:
                    end = mid
            length[start] = num
            max_val = max(start + 1, max_val)
        return max_val

    def lengthOfLIS_n2(self, nums):
        max_val, dp = 0, []
        for i in range(len(nums)):
            val = 0
            for j in range(i):
                if nums[i] > nums[j] and dp[j] > val:
                    val = dp[j]
            dp.append(val + 1)
            max_val = max(dp[i], max_val)
        return max_val
