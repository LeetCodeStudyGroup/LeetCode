class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return n
        elif n <= 3: return n - 1
        two, three = 1, 0
        for _ in range(n - 2):
            if two > 0:
                two -= 1
                three += 1
            else:
                two += 2
                three -= 1
        return 2 ** two * 3 ** three
