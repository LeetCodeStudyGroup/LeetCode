class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        check = False
        i = j = 0
        while i < len(nums) - 1:
            nums[j] = nums[i]
            if nums[i] == nums[i + 1]:
                if check:
                    j -= 1
                else:
                    check = True
            else:
                check = False
            i += 1
            j += 1
        nums[j] = nums[i]
        return j + 1
