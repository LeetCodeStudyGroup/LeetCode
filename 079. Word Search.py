class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        if row == 0 or len(word) == 0:
            return False
        col = len(board[0])
        mask = [[True for x in range(col)] for y in range(row)]
        start_list = []
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    start_list.append((i, j))
        for i, j in start_list:
            mask[i][j] = False
            if self.check(board, word, mask, i, j, 1):
                return True
            mask[i][j] = True
        return False

    def check(self, board, word, mask, i, j, str_inx):
        if str_inx == len(word):
            return True
        for x, y in self.find(board, mask, i, j, word[str_inx]):
            mask[x][y] = False
            if self.check(board, word, mask, x, y, str_inx + 1):
                return True
            mask[x][y] = True
        return False

    def find(self, board, mask, i, j, c):
        result = []
        if i + 1 < len(mask) and mask[i + 1][j] and board[i + 1][j] == c:
            result.append((i + 1, j))
        if i - 1 >= 0 and mask[i - 1][j] and board[i - 1][j] == c:
            result.append((i - 1, j))
        if j + 1 < len(mask[0]) and mask[i][j + 1] and board[i][j + 1] == c:
            result.append((i, j + 1))
        if j - 1 >= 0 and mask[i][j - 1] and board[i][j - 1] == c:
            result.append((i, j - 1))
        return result
