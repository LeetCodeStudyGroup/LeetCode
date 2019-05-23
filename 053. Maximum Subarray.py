import sys

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum_array = []
        for i in range(0, len(nums)):
            if i == 0:
                sum_array.append(nums[0])
            else:
                sum_array.append(sum_array[i-1] + nums[i])
             
        max_subarray = -sys.maxsize -1
        min_subarray = sys.maxsize
        
        for i in range(0, len(nums)):
            if sum_array[i] > max_subarray:
                max_subarray = sum_array[i]
            
            max_subarray = max(max_subarray, sum_array[i] - min_subarray)
            
            if sum_array[i] < min_subarray:
                min_subarray = sum_array[i]
    
        return max_subarray
