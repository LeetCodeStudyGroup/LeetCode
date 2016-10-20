class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.do_search(nums, target, 0, len(nums) - 1)
        
    def do_search(self, nums, target, start, end):
        if start > end:
            return -1
        mid = (start + end) / 2
        if target == nums[mid]:
            return mid
        if nums[start] > nums[end]:
            x = self.do_search(nums, target, mid + 1, end)
            if x == -1:
                return self.do_search(nums, target, start, mid - 1)
            return x
        else:
            if target > nums[mid]:
                return self.do_search(nums, target, mid + 1, end)
            if target < nums[mid]:
                return self.do_search(nums, target, start, mid - 1)
