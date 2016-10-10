class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for i in range(len(nums)):
            single ^= nums[i]
        return single
