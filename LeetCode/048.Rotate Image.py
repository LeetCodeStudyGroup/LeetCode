class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while n - i * 2 > 1:
            j = i
            while j < n - i - 1:
                x, y = i, j
                tmp = matrix[x][y]
                for k in range(3):
                    matrix[x][y] = matrix[n - y - 1][x]
                    x, y = n - y - 1, x
                matrix[x][y] = tmp
                j += 1
            i += 1
