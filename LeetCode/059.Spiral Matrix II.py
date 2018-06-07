class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(n):
            result.append([0] * n)
        num = 1
        r = 0
        while r < n - r:
            i = r
            while i < n - r:
                result[r][i] = num
                num += 1
                i += 1

            i = r + 1
            while i < n - r - 1:
                result[i][n - r - 1] = num
                num += 1
                i += 1

            if r < n - r - 1:
                i = n - r - 1
                while i >= r:
                    result[n - r - 1][i] = num
                    num += 1
                    i -= 1

                i = n - r - 2
                while i > r:
                    result[i][r] = num
                    num += 1
                    i -= 1
            r += 1
        return result
            
