class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        limit, record = {}, set()
        self.count = 0
        self.setup(limit)
        for num in range(m, n + 1):
            for i in range(1, 10):
                self.find(limit, num - 1, record, i)
        return self.count

    def find(self, limit, n, record, cur):
        if n == 0:
            self.count += 1
            return
        record.add(cur)
        for nxt in range(1, 10):
            if nxt not in record and (nxt not in limit[cur] or limit[cur][nxt] in record):
                self.find(limit, n - 1, record, nxt)
        record.remove(cur)

    def setup(self, steps):
        steps[1] = {3: 2, 9: 5, 7: 4}
        steps[2] = {8: 5}
        steps[3] = {1: 2, 7: 5, 9: 6}
        steps[4] = {6: 5}
        steps[5] = {}
        steps[6] = {4: 5}
        steps[7] = {1: 4, 3: 5, 9: 8}
        steps[8] = {2: 5}
        steps[9] = {1: 5, 3: 6, 7: 8}
