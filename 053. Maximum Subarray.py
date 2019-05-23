import sys

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums is None:
            return None
        
        if len(nums) == 0:
            return []
        
        maxResult = nums[0]
        tempSum = nums[0]

        for idx in range(1,len(nums)):
            if tempSum < 0:
                tempSum = nums[idx]
            else:
                tempSum += nums[idx]
                         
            if maxResult < tempSum:
                maxResult = tempSum
        
        return maxResult
