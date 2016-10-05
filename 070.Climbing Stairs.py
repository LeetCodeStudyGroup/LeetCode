class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climb({1:1, 2:2}, n)
        
    def climb(self, mem, n):
        if n not in mem:
            mem[n] = self.climb(mem, n - 1) + self.climb(mem, n - 2)
        return mem[n]
