class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        peak = nums[0]
        peak_index = 0
        is_find = False
        i = 1
        while i < len(nums):
            if nums[i] == peak:
                is_find = False
            elif nums[i] > peak:
                peak = nums[i]
                peak_index = i
            elif nums[i] < nums[i - 1]:
                if is_find and i > peak_index * 2:
                    return peak_index
                is_find = True
            i += 1
        return peak_index
