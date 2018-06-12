public class Solution {
    /**
     * @param A: A string
     * @param B: A string
     * @return: The length of longest common subsequence of A and B
     */
    public int longestCommonSubsequence(String A, String B) {
        // write your code here
        int n = A.length(), m = B.length();
        int[][] dp = new int[n + 1][m + 1];
        int max = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dp[i + 1][j + 1] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                if (A.charAt(i) == B.charAt(j)) {
                    dp[i + 1][j + 1] = Math.max(dp[i + 1][j + 1], dp[i][j] + 1);
                }
                max = Math.max(max, dp[i + 1][j + 1]);
            }
        }
        return max;
    }
}
