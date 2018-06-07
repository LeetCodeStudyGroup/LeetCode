class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0:
            return 0

        def env_cmp(e1, e2):
            if e1[0] == e2[0]:
                return e2[1] - e1[1]
            return e1[0] - e2[0]
        envelopes.sort(cmp=env_cmp)

        return self.dp_nlog(envelopes)

    def dp_nlog(self, envelopes):
        from bisect import bisect_left
        length, dp = 0, [0] * len(envelopes)
        for i, envelope in enumerate(envelopes):
            index = bisect_left(dp, envelope[1], 0, length)
            dp[index] = envelope[1]
            if index == length:
                length += 1
        return length

    def dp_n2(self, envelopes):
        rst, dp = 1, [1] * len(envelopes)
        for i in range(len(envelopes)):
            for j in range(i, -1, -1):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            rst = max(rst, dp[i])
        return rst
