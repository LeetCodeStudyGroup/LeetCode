class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0

        i, j = 0, len(nums) - 1
        while i + 1 < len(nums) and nums[i] <= nums[i + 1]:
            i += 1
        while j - 1 >= 0 and nums[j] >= nums[j - 1]:
            j -= 1

        if j == 0:
            return 0

        min_val = min(nums[i:j + 1])
        max_val = max(nums[i:j + 1])
        start, end = 0, len(nums) - 1
        while start < i and nums[start] <= min_val:
            start += 1
        while end > j and nums[end] >= max_val:
            end -= 1
        return end - start + 1
