class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.search(nums, 0, len(nums) - 1)
        
    def search(self, nums, start, end):
        if nums[start] <= nums[end]:
            return nums[start]
        else:
            mid = (start + end) / 2
            return min(self.search(nums, start, mid), self.search(nums, mid + 1, end))
