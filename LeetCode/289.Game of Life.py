class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0: return
        n = len(board[0])
        matrix = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        record = [[False for x in range(n)] for y in range(m)]
        for i in range(m):
            for j in range(n):
                self.update(matrix, record, board, m, n, i, j)

    def update(self, matrix, record, board, m, n, i, j):
        if record[i][j]:
            return
        record[i][j] = True
        cnt = self.get_neighbor(matrix, board, m, n, i, j)
        new_val = 1 if cnt == 3 or (cnt == 2 and board[i][j] == 1) else 0
        if board[i][j] != new_val:
            for x, y in matrix:
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n:
                    continue
                self.update(matrix, record, board, m, n, new_i, new_j)
            board[i][j] = new_val

    def get_neighbor(self, matrix, board, m, n, i, j):
        count = 0
        for x, y in matrix:
            new_i, new_j = i + x, j + y
            if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n:
                continue
            if board[new_i % m][new_j % n] == 1:
                count += 1
        return count
