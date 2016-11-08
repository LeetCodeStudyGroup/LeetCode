class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        table = {}
        for num in nums:
            if num in table:
                return True
            else:
                table[num] = True
        return False
