class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

    def judgeCircle2(self, moves):
        x, y = 0, 0
        for move in moves:
            if move == 'U':
                x += 1
            elif move == 'D':
                x -= 1
            elif move == 'L':
                y -= 1
            elif move == 'R':
                y += 1
        return x == 0 and y == 0
