class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0: return False
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        mark = [[False for x in range(n)] for y in range(m)]
        go_right = False
        col = row = 0
        while row >= 0 and col >= 0 and row < m and col < n and not mark[row][col]:
            mark[row][col] = True
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                if go_right:
                    if col + 1 == n or matrix[row][col + 1] > target:
                        row += 1
                    else:
                        col += 1
                else:
                    if row + 1 == m or matrix[row + 1][col] > target:
                        col += 1
                    else:
                        row +=1
            else:
                if go_right:
                    if col - 1 < 0:
                        go_right = not go_right
                        row -= 1
                    else:
                        col -= 1
                else:
                    if row - 1 < 0:
                        go_right = not go_right
                        col -= 1
                    else:
                        row -=1
        return False
