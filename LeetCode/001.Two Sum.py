class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if (nums[i] + nums[(j + i + 1)]) == target:
                    return [i , j + i + 1]
        return []

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        i = 0
        while i < len(nums):
            tmp = target - nums[i]
            if tmp in maps:
                return [maps[tmp], i]
            maps[nums[i]] = i
            i += 1
        return []
