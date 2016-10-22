class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        return self.find(nums, target, 0, len(nums) - 1)
        
    def find(self, nums, target, start, end):
        if start > end:
            return False
        mid = (start + end) / 2
        if nums[mid] == target:
            return True
        if nums[start] > nums[end] or nums[start] == nums[end]:
            ret = self.find(nums, target, start, mid - 1)
            if not ret:
                ret = self.find(nums, target, mid + 1, end)
            return ret
        if nums[mid] > target:
            return self.find(nums, target, start, mid - 1)
        else:
            return self.find(nums, target, mid + 1, end)
