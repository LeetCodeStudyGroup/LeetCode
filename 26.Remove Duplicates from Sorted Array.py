class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = i + 1
        ret = len(nums)
        while j < len(nums):
            if nums[i] != nums[j]:
                nums[i + 1] = nums[j]
                i += 1
            else:
                ret -= 1
            j += 1
        return ret
