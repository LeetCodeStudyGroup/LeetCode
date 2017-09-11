class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rst = []
        if len(s) <= 1:
            return rst

        ary = list(s)
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                tmp = ary[:]
                tmp[i] = '-'
                tmp[i + 1] = '-'
                rst.append(''.join(tmp))
        return rst
