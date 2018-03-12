import math

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = int(start + (end - start)/2)

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid

            elif nums[mid] > target:
                end = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        for index in range(0, len(nums)):
            if target < nums[index]:
                return index

        return len(nums)
