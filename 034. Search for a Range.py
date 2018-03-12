class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if nums == None or nums == []:
            return [-1, -1]
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = int(start + (end - start)/2)
            
            if nums[mid] == target:
                lefttest = self.findTheLeftest(nums, mid, end, target)
                rightest = self.findTheRightest(nums, start, mid, target)
                return [lefttest, rightest]
                
            elif nums[mid] < target:
                start = mid
            elif nums[mid] > target:
                end = mid
                
        if nums[start] == target and nums[end] == target:
            return [start, end]
        
        if nums[start] == target:
            return [start, start]
        
        if nums[end] == target:
            return [end, end]
        
        return [-1, -1]
        
        
    # findTheLeftest() - 再用 binary search 找... 但懶了...用暴力法推
    def findTheLeftest(self, nums, start, end, target):
        for index, num in enumerate(nums):
            if num == target:
                return index
        
        return start
    
    # findTheRightest() - 再用 binary search 找... 
    def findTheRightest(self, nums, start, end, target):
        for index, num in reversed(list(enumerate(nums))):
            if num == target:
                return index
        
        return end
    
    
