class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sets, duplicate, sum_val = set(), 0, (1 + len(nums)) * len(nums) / 2
        for num in nums:
            if num in sets:
                duplicate = num
            sum_val -= num
            sets.add(num)
        return [duplicate, sum_val + duplicate]

    def findErrorNums2(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                tmp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = tmp
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
        return None
