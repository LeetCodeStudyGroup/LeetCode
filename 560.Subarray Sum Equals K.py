class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        presum = defaultdict(int)
        presum[0] = 1
        rst, val = 0, 0
        for num in nums:
            val += num
            rst += presum[val - k]
            presum[val] += 1
        return rst
