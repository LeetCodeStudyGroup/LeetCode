class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        cur = i = 1
        while i <= n:
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            elif  cur + 1 <= n and cur % 10 != 9:
                cur += 1
            else:
                while (cur / 10) % 10 == 9:
                    cur /= 10
                cur = cur / 10 + 1
            i += 1
        return res

    def lexicalOrder2(self, n):
        res = []
        self.do_add(res, n, 1)
        return res

    def do_add(self, res, n, num):
        res.append(num)
        if num * 10 <= n:
            self.do_add(res, n, num * 10)
        if num + 1 <= n and num % 10 != 9:
            self.do_add(res, n, num + 1)
