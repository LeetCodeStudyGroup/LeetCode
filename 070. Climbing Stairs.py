class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        mapping = {}
        mapping[0] = 0
        mapping[1] = 1
        mapping[2] = 2
        
        for i in range(3, n+1):
            mapping[i] = mapping[i-1] + mapping[i-2]
        
        return mapping[n]
