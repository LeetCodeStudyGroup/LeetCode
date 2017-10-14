class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        freq, created = defaultdict(int), defaultdict(int)
        for num in nums:
            freq[num] += 1
        for num in nums:
            if freq[num] == 0:
                continue
            elif created[num] > 0:
                created[num] -= 1
                created[num + 1] += 1
            elif freq[num + 1] > 0 and freq[num + 2] > 0:
                freq[num + 1] -= 1
                freq[num + 2] -= 1
                created[num + 3] += 1
            else:
                return False
            freq[num] -= 1
        return True
