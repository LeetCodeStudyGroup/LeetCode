class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        nums = [True] * n
        nums[0] = nums[1] = False
        for i in range(2, int((n - 1)**0.5) + 1):
            if nums[i]:
                for j in range(i * 2, n, i):
                    if nums[j]:
                        nums[j] = False
        return nums.count(True)
