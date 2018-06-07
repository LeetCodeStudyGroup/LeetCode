class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.rst = []
        num = [0] * n
        if n % 2 == 1:
            for x in ['0', '1', '8']:
                num[n / 2] = x
                self.dfs(num, 0, n - 1)
        else:
            self.dfs(num, 0, n - 1)

        return self.rst

    def dfs(self, num, i, j):
        if i >= j:
            self.rst.append(''.join(num))
            return

        for x, y in [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]:
            if i == 0 and x == '0':
                continue
            next_num = num[:]
            next_num[i] = x
            next_num[j] = y
            self.dfs(next_num, i + 1, j - 1)
