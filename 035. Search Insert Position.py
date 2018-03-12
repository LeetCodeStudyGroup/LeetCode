import math

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        ## 嘗試找出 target 在數列中的範圍
        while start + 1 < end:
            mid = int(start + (end - start)/2)

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                start = mid

            elif nums[mid] > target:
                end = mid

        ## 測試 target 是否在數列中
        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        ## 確認 target 不存在數列中
        # target < 數列最左邊
        if target < nums[0]:
            return 0
        
        # target > 數列最右邊
        if target > nums[-1]:
            return len(nums)
        
        # target 在數列中間
        return end
    
