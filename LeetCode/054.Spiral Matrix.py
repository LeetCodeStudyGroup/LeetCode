class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        i = 0
        m = len(matrix)
        if m <= 0:
            return []
        n = len(matrix[0])
        round = min(m, n)
        while i < round - i:
            j = i
            while j < n - i:
                result.append(matrix[i][j])
                j += 1
            j = i + 1
            while j < m - i - 1:
                result.append(matrix[j][n - 1 - i])
                j += 1
            if m - 1 - i > i:
                j = n - 1 - i
                while j >= i:
                    result.append(matrix[m - 1 - i][j])
                    j -= 1
            if n - 1 - i > i:
                j = m - 1 - i - 1
                while j > i:
                    result.append(matrix[j][i])
                    j -= 1
            i += 1
        return result
