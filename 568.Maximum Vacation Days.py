class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if len(days) == 0 or len(days[0]) == 0:
            return 0

        dp = [0] * len(flights)
        for i in range(len(days[0]) - 1, -1, -1):
            nextdp  = [0] * len(flights)
            for j in range(len(flights)):
                for k in range(len(flights)):
                    if flights[k][j] == 1 or j == k:
                        nextdp[k] = max(nextdp[k], dp[j] + days[k][i])
            dp = nextdp

        max_day = 0
        for i in range(len(flights)):
            if flights[0][i] == 1 or i == 0:
                max_day = max(max_day, dp[i])
        return max_day
