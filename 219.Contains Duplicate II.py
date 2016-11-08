class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        table = {}
        for i in range(len(nums)):
            if nums[i] in table and i - table[nums[i]] <= k:
                return True
            else:
                table[nums[i]] = i
        return False
