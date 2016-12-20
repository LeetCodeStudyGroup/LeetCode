class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[(nums[i] - 1) % len(nums)] += len(nums)
        return filter(lambda i: nums[i - 1] <= len(nums), range(1, len(nums) + 1))

    def findDisappearedNumbers2(self, nums):
        for i in range(len(nums)):
            inx = nums[i] - 1
            while inx + 1 != nums[inx]:
                nums[inx], inx = inx + 1, nums[inx] - 1
        return filter(lambda i: nums[i - 1] != i, range(1, len(nums) + 1))
