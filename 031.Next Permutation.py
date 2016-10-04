class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        rep = len(nums) - 1
        while rep > 0:
            if nums[rep] > nums[rep - 1]:
                break
            rep -= 1
        if rep == 0:
            i = 0
            while i < (len(nums) - 1 - i):
                nums[i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[i]
                i += 1
        else:
            rep -= 1
            i = len(nums) - 1
            while i > rep:
                if nums[i] > nums[rep]:
                    break
                i -= 1
            nums[rep], nums[i] = nums[i], nums[rep]
            i = rep + 1
            while i < len(nums):
                j = i + 1
                while j < len(nums):
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                    j += 1
                i += 1
