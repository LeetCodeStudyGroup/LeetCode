/**
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
*/

class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0)
            return 0;
        Arrays.sort(coins);
        int[] minCounts = new int[amount + 1];
        for (int i = 1; i <= amount; i++) {
            int min = 100001;
            for (int j = coins.length - 1; j >= 0; j--) {
                int rest = i - coins[j];
                if (rest < 0)
                    continue;
                if (minCounts[rest] != -1) {
                    minCounts[i] = minCounts[rest] + 1;
                    if (minCounts[i] < min)
                        min = minCounts[i];
                }
            }
            if (min == 100001)
                minCounts[i] = -1;
            else 
                minCounts[i] = min;
        }
        
        return minCounts[amount] != 0 ? minCounts[amount]: -1;
    }
}
