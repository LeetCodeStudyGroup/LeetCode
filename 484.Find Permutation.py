class Solution(object):
    def findPermutation(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        if len(s) == 0:
            return [1]
        rst = []
        num, i = 1, 0
        if s[0] == 'I':
            rst.append(1)
        while i < len(s):
            d_cnt, i_cnt = 0, 0
            while i < len(s) and s[i] == 'I':
                i_cnt += 1
                i += 1
            while i < len(s) and s[i] == 'D':
                d_cnt += 1
                i += 1
            self.consist(rst, num, d_cnt, i_cnt)
            num += d_cnt + i_cnt
        return rst

    def consist(self, rst, num, d_cnt, i_cnt):
        for n in range(num + 1, num + i_cnt):
            rst.append(n)
        rst.append(num + d_cnt + i_cnt)
        for n in range(num + d_cnt + i_cnt - 1, num + i_cnt - 1, -1):
            rst.append(n)
