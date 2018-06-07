class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        ary, max_cnt = self.get_arithmetic(A)
        if max_cnt < 2: return 0

        dp = [0] * (max_cnt + 1)
        dp[2] = 1
        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] * 2 - dp[i - 2] + 1
        rst = 0
        for i in ary:
            rst += dp[i]
        return rst

    def get_arithmetic(self, A):
        ary, cnt, max_cnt = [], 1, 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                cnt += 1
            else:
                if cnt > 1:
                    ary.append(cnt)
                max_cnt, cnt = max(max_cnt, cnt), 1
        if cnt > 1:
            ary.append(cnt)
        max_cnt = max(max_cnt, cnt)
        return ary, max_cnt
