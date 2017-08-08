class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        count = i = 1
        while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1
        if i < len(nums):
            is_pos = nums[i] < nums[i - 1]

        while i < len(nums):
            if (is_pos and nums[i - 1] > nums[i]) or (not is_pos and nums[i - 1] < nums[i]):
                count += 1
                is_pos = not is_pos
            i += 1
        return count
