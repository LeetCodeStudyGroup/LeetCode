public class Solution {
    /**
     * @param values: a vector of integers
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int[] values) {
        // write your code here
        int n = values.length;
        int[] sum = new int[n + 1];
        int[][] dp = new int[n][n];

        for (int i = 0; i < n; i++) {
            sum[i + 1] = sum[i] + values[i];
        }

        for (int i = 0; i < n; i++) {
            dp[i][0] = values[i];
        }

        for (int i = 1; i < n; i++) {
            for (int j = n - i - 1; j >= 0; j--) {
                int left = values[j] + sum[j + i + 1] - sum[j + 1] - dp[j + 1][i - 1];
                int right = values[j + i] + sum[j + i] - sum[j] - dp[j][i - 1];
                dp[j][i] = Math.max(left, right);
            }
        }

        return dp[0][n - 1] * 2 > sum[n];
    }
}
