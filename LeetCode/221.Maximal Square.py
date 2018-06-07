class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        high, left, right = [0] * n, [0] * n, [n] * n
        max_area = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                high[j] = high[j] + 1 if matrix[i][j] == '1' else 0

            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(cur_left, left[j])
                else:
                    left[j], cur_left = 0, j + 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(cur_right, right[j])
                else:
                    right[j], cur_right = n, j

            for j in range(n):
                max_area = max(max_area, pow(min(right[j] - left[j], high[j]), 2))
        return max_area
