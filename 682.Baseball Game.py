class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        rst, points = 0, []
        for op in ops:
            if op == 'C':
                rst -= points[-1]
                points.pop()
            elif op == 'D':
                points.append(points[-1] * 2)
                rst += points[-1]
            elif op == '+':
                points.append(points[-1] + points[-2])
                rst += points[-1]
            else:
                points.append(int(op))
                rst += points[-1]
        return rst
