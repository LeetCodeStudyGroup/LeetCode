class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        inx_2 = None
        while i <= j:
            if nums[i] == 0:
                if inx_2 != None:
                    nums[i], nums[inx_2] = nums[inx_2], nums[i]
                    inx_2 += 1
                i += 1
            elif nums[i] == 1:
                if inx_2 == None:
                    inx_2 = i
                i += 1
            elif nums[i] == 2:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
