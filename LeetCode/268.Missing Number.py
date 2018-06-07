class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums) * (len(nums) + 1) / 2
        for num in nums:
            missing -= num
        return missing
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing
        #return reduce(lambda x, y: x ^ y, range(len(nums) + 1)) ^ reduce(lambda x, y: x ^ y, nums)

    def sum(self, nums):
        missing = len(nums) * (len(nums) + 1) / 2
        for num in nums:
            missing -= num
        return missing
