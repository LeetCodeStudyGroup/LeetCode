class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        if m == 0: return
        n = len(matrix[0])
        self.area = [[0 for x in range(n + 1)] for y in range(m + 1)]
        for i in range(m):
            s = 0
            for j in range(n):
                s += matrix[i][j]
                self.area[i + 1][j + 1] = s + self.area[i][j + 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.area[row2 + 1][col2 + 1] - self.area[row1][col2 + 1] - self.area[row2 + 1][col1] + self.area[row1][col1]

class NumMatrix2(object):
    def __init__(self, matrix):
        self.row = []
        self.col = []
        for i in range(len(matrix)):
            self.row.append([])
            val = 0
            for num in matrix[i]:
                val += num
                self.row[i].append(val)

    def sumRegion(self, row1, col1, row2, col2):
        val = 0
        for i in range(row1, row2 + 1):
            val += self.row[i][col2]
            if col1 > 0:
                val -= self.row[i][col1 - 1]
        return val

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
