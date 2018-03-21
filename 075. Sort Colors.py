class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        curt = 0
        
        while curt <= right:
            if nums[curt] == 0:
                nums[left], nums[curt] = nums[curt], nums[left]
                left += 1
                curt += 1
            elif nums[curt] == 2:
                nums[right], nums[curt] = nums[curt], nums[right]
                right -= 1
            else:
                curt += 1
