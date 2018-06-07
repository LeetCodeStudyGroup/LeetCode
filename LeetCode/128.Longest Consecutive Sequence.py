class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pool = {}
        times = {}
        longest = 1
        for num in nums:
            if num in pool:
                continue
            if num + 1 in pool and num - 1 in pool:
                pool[num] = num
                times[num] = times[pool[num + 1]] + times[pool[num - 1]]
                pool[num - times[pool[num - 1]]] = num
                pool[num + times[pool[num + 1]]] = num
            elif num + 1 in pool:
                pool[num] = pool[num + 1]
            elif num - 1 in pool:
                pool[num] = pool[num - 1]
            else:
                pool[num], times[num] = num, 0
            times[pool[num]] += 1
            if times[pool[num]] > longest:
                longest = times[pool[num]]
        return longest
