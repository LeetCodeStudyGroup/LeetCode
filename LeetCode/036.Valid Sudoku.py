class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            records = [{}, {}, {}]
            for j in range(9):
                points = [board[i][j],board[j][i], board[(i/3) * 3 + (j/3)][(i%3) * 3 + (j%3)]]
                for n in range(3):
                    if not self.check_point(records[n], points[n]):
                        return False
        return True
        
    def check_point(self, record, point):
        if point != ".":
            if point in record:
                return False
            record[point] = True
        return True
