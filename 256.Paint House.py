class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0

        dp = [[0] * (len(costs) + 1) for _ in range(3)]
        for i, cost in enumerate(costs):
            dp[0][i + 1] = min(dp[1][i], dp[2][i]) + cost[0]
            dp[1][i + 1] = min(dp[0][i], dp[2][i]) + cost[1]
            dp[2][i + 1] = min(dp[0][i], dp[1][i]) + cost[2]
        return min(dp[0][-1], dp[1][-1], dp[2][-1])
