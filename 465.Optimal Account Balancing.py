from collections import defaultdict
import sys

class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        bal = defaultdict(int)
        for t in transactions:
            bal[t[0]] -= t[2]
            bal[t[1]] += t[2]
        debt = []
        return self.dfs(sorted(bal.values()), 0, 0)

    def dfs(self, debt, start, cnt):
        while start < len(debt) and debt[start] == 0:
            start += 1
        res, prev = sys.maxint, 0
        for i in range(start + 1, len(debt)):
            if debt[i] != prev and debt[i] * debt[start] < 0:
                debt[i] += debt[start]
                res = min(res, self.dfs(debt, start + 1, cnt + 1))
                debt[i] -= debt[start]
                prev = debt[i]
        return cnt if res == sys.maxint else res
