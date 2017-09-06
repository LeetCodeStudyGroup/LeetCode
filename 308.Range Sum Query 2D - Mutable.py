class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            self.bit = None
            return
        self.n, self.m = len(matrix), len(matrix[0])
        self.nums = [[0] * (len(matrix[0])) for _ in range((len(matrix)))]
        self.bit = [[0] * (len(matrix[0]) + 1) for _ in range((len(matrix) + 1))]
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                self.update(i, j, num)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        if row > self.n or col > self.m:
            return
        delta = val - self.nums[row][col]
        i = row + 1
        self.nums[row][col] = val
        while i <= self.n:
            j = col + 1
            while j <= self.m:
                self.bit[i][j] += delta
                j += j & -j
            i += i & -i

    def sum(self, row, col):
        rst = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                rst += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return rst

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 > row2 or col1 > col2 or row2 > self.n or col2 > self.m:
            return 0
        return self.sum(row2, col2) - self.sum(row2, col1 - 1) - self.sum(row1 - 1, col2) + self.sum(row1 - 1, col1 - 1)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
