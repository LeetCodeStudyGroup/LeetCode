class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            return self.search(nums, target, 0, len(nums) - 1)
        
    def search(self, nums, target, start, end):
        if start >= end:
            return start
        mid = (start + end) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target and nums[mid + 1] > target:
            return mid + 1
        elif nums[mid] > target:
            return self.search(nums, target, start, mid)
        else:
            return self.search(nums, target, mid + 1, end)
