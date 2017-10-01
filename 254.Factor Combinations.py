class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rst = []
        self.helper(rst, [], 2, n)
        return rst

    def helper(self, rst, cur, i, n):
        while i * i <= n:
            if n % i == 0:
                r = cur[:] + [i, n / i]
                rst.append(r)
                cur.append(i)
                self.helper(rst, cur, i, n / i)
                cur.pop()
            i += 1
