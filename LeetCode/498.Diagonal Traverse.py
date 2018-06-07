class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rst = []
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return rst

        i, j, up = 0, 0, True
        while i < len(matrix) and j < len(matrix[0]):
            rst.append(matrix[i][j])
            i, j = self.move(up, i, j)

            if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
                if up:
                    i += 1
                else:
                    j += 1
                up = not up

            if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
                i, j = self.move(up, i, j)
        return rst

    def move(self, up, i, j):
        return i - 1, j + 1 if up else i + 1, j - 1
