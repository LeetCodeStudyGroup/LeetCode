class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.search(nums, target, 0, len(nums) - 1)
        
        
    def search(self, nums, target, start, end):
        if nums[start] <= target and nums[end] >= target:
            if end == start:
                if nums[start] == target:
                    return start, start
                else:
                    return (-1, -1)
            mid = (start + end) / 2
            result = []
            result.extend(self.search(nums, target, start, mid))
            result.extend(self.search(nums, target, mid + 1, end))
            ret = (-1, -1)
            for r in result:
                if ret[0] == -1 and r != -1:
                    ret = r, -1
                elif ret[0] != -1 and r != -1:
                    ret = ret[0], r
            return ret
        else:
            return (-1, -1)
