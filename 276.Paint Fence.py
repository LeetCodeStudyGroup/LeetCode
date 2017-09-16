class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        diff, same = k * (k - 1), k
        for i in range(2, n):
            diff, same = (same + diff) * (k - 1), diff
        return same + diff

    def numWays2(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        diff_dp = [k * (k - 1)]
        same_dp = [k]
        for i in range(2, n):
            diff_dp.append((same_dp[-1] + diff_dp[-1]) * (k - 1))
            same_dp.append(diff_dp[-2])
        return same_dp[-1] + diff_dp[-1]
