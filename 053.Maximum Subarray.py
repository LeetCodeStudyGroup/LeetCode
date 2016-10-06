class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = None
        val = 0
        for n in nums:
            val += n
            if max_sum == None or val > max_sum:
                max_sum = val
            if val < 0:
                val = 0
        return max_sum if max_sum else 0
