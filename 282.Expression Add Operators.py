class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        rst = []
        self.checking(rst, num, target, 0, '', 0, 0)
        return rst

    def checking(self, res, num, target, inx, exp, val, muled):
        if inx == len(num):
            if val == target:
                res.append(exp)
            return
        for i in range(inx, len(num)):
            if i != inx and num[inx] == '0':
                continue
            x = int(num[inx:i + 1])
            if inx == 0:
                self.checking(res, num, target, i + 1, exp + str(x), x, x)
            else:
                self.checking(res, num, target, i + 1, exp + '+' + str(x), val + x, x)
                self.checking(res, num, target, i + 1, exp + '-' + str(x), val - x, -x)
                self.checking(res, num, target, i + 1, exp + '*' + str(x), val - muled + muled * x, muled * x)
