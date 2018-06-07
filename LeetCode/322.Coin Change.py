class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0: return 0
        coins = list(reversed(sorted(coins)))
        dp, stack = {0:0}, [0]
        while len(stack) > 0:
            next = []
            for val in stack:
                for coin in coins:
                    next_val = coin + val
                    if next_val not in dp:
                        dp[next_val] = dp[val] + 1
                        if next_val == amount:
                            return dp[next_val]
                        if next_val < amount:
                            next.append(next_val)
            stack = next
        return -1

    def coinChange_TLE(self, coins, amount):
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = amount + 1
            for j in range(len(coins)):
                val = i - coins[j]
                if val >= 0 and dp[val] != -1:
                    dp[i] = min(dp[val] + 1, dp[i])
            if dp[i] == amount + 1:
                dp[i] = -1
        return dp[amount]
