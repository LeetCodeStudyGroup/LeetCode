class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import sys
        is_modify = False
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] > nums[i + 1]:
                if is_modify:
                    return False

                is_modify = True
                if i + 2 < len(nums):
                    if nums[i] > nums[i + 2]:
                        nums[i] = nums[i - 1] if i > 0 else 1
                    else:
                        nums[i + 1] = nums[i]

                    if nums[i] > nums[i + 1]:
                        return False
        return True
