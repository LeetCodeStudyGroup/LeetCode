class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row = self.search_col(matrix, target, 0, len(matrix) - 1)
        return self.search_row(matrix[row], target, 0, len(matrix[0]) - 1)

    def search_col(self, matrix, target, start, end):
        mid = (start + end) / 2
        if mid + 1 < len(matrix) and matrix[mid][0] <= target and matrix[mid + 1][0] > target:
            return mid
        elif matrix[mid][0] > target:
            if mid == 0:
                return 0
            return self.search_col(matrix, target, start, mid - 1)
        else:
            if mid == len(matrix) - 1:
                return mid
            return self.search_col(matrix, target, mid + 1, end)

    def search_row(self, matrix_row, target, start, end):
        if start > end:
            return False
        mid = (start + end) / 2
        if matrix_row[mid] == target:
            return True
        elif matrix_row[mid] > target:
            return self.search_row(matrix_row, target, start, mid - 1)
        else:
            return self.search_row(matrix_row, target, mid + 1, end)

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        i = j = 0
        while i < len(matrix):
            if matrix[i][0] > target:
                break
            i += 1
        i = i - 1 if i != 0 else 0
        while j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            j += 1
        return False
