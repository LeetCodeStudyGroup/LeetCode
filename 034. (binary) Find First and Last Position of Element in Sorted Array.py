class Solution:
    # right 已經是 target, 只是要找到最左邊的 target 在哪
    def findLeftTarget(self, nums, target: int, left: int, right: int):
        while left + 1 < right:
            mid = left + int((right - left) / 2)
            
            if nums[mid] < target:
                left = mid
            elif nums[mid] == target:
                right = mid
                left = self.findLeftTarget(nums, target, left, right)
            
        if nums[left] == target:
            return left
        else:
            return right
    
    # left 已經是 target, 只是要找到最右邊的 target 在哪
    def findRightTarget(self, nums, target: int, left: int, right: int):
        while left + 1 < right:
            mid = left + int((right - left) / 2)
            
            if nums[mid] > target:
                right = mid
            elif nums[mid] == target:
                left = mid
                right = self.findRightTarget(nums, target, left, right)
        
        if nums[right] == target:
            return right
        else:
            return left
    
    def searchRange(self, nums, target: int) -> list:
        if nums is None or len(nums) == 0:
            return [-1, -1]
        
        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        
        
        while left + 1 < right:
            mid = left + int((right - left) / 2)
            
            if nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = self.findLeftTarget(nums, target, left, mid)
                right = self.findRightTarget(nums, target, mid, right)
                return [left, right]
        

        if nums[left] == target and nums[right] == target:
            return [left, right]

        if nums[left] == target:
            return [left, left]

        if nums[right] == target:
            return [right, right]
        
        return [-1,-1]
