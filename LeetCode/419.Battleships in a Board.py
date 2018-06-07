class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m = len(board)
        if m == 0: return 0
        n = len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1]== '.'):
                    count += 1
        return count

    def countBattleships2(self, board):
        m = len(board)
        if m == 0: return 0
        n = len(board[0])
        record = [[False if board[x][y] == 'X' else True for y in range(n)] for x in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not record[i][j]:
                    self.get_length(record, m, n, i, j)
                    count += 1
        return count

    def get_length(self, record, m, n, i, j):
        record[i][j] = True
        count = 1
        down = i + 1
        while down < m and not record[down][j]:
            record[down][j] = True
            count += 1
            down += 1
        right = j + 1
        while right < n and not record[i][right]:
            record[i][right] = True
            count += 1
            right += 1
        return count
