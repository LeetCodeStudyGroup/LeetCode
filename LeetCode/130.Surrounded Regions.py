class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0: return
        n = len(board[0])
        record = [[False if board[x][y] == 'O' else True for y in range(n)] for x in range(m)]
        for i in range(m):
            self.BFS(record, board, m, n, i, 0)
            self.BFS(record, board, m, n, i, n - 1)
        for i in range(n):
            self.BFS(record, board, m, n, 0, i)
            self.BFS(record, board, m, n, m - 1, i)
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if not record[i][j]:
                    board[i][j] = 'X'

    def BFS(self, record, board, m, n, x, y):
        if record[x][y]: return
        stack = [(x, y)]
        while len(stack) > 0:
            i, j = stack.pop()
            record[i][j] = True
            if i + 1 < m and not record[i + 1][j]: stack.append((i + 1, j))
            if i > 0 and not record[i - 1][j]: stack.append((i - 1, j))
            if j + 1 < n and not record[i][j + 1]: stack.append((i, j + 1))
            if j > 0 and not record[i][j - 1]: stack.append((i, j - 1))

    def DFS(self, record, board, m, n, i, j):
        if record[i][j]: return
        record[i][j] = True
        if i + 1 < m: self.DFS(record, board, m, n, i + 1, j)
        if i > 0: self.DFS(record, board, m, n, i - 1, j)
        if j + 1 < n: self.DFS(record, board, m, n, i, j + 1)
        if j > 0: self.DFS(record, board, m, n, i, j - 1)
