class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        for i in range(32):
            cnt = [0, 0]
            for j in range(len(nums)):
                cnt [nums[j] & 1] += 1
                nums[j] = nums[j] >> 1
            total += cnt[0] * cnt[1]
        return total
