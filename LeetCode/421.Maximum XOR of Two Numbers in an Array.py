class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_val, mask = 0, 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            sets = set()
            for num in nums:
                sets.add(num & mask)
            tmp = max_val | (1 << i)
            for num in sets:
                if tmp ^ num in sets:
                    max_val = tmp
                    break
        return max_val
