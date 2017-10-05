class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.row = [[0] * n, [0] * n]
        self.col = [[0] * n, [0] * n]
        self.dia = [[0, 0], [0, 0]]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.row[player - 1][row] += 1
        self.col[player - 1][col] += 1
        if row == col:
            self.dia[player - 1][0] += 1
        if row + col == self.n - 1:
            self.dia[player - 1][1] += 1

        if self.row[player - 1][row] == self.n or \
           self.col[player - 1][col] == self.n or \
           self.dia[player - 1][0] == self.n or \
           self.dia[player - 1][1] == self.n:
            return player
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
