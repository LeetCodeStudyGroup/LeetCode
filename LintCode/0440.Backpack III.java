public class Solution {
    /**
     * @param A: an integer array
     * @param V: an integer array
     * @param m: An integer
     * @return: an array
     */
    public int backPackIII(int[] A, int[] V, int m) {
        // write your code here
        int n = A.length;
        int[] dp = new int[m + 1];
        int max = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= m; j++) {
                int nextSize = j + A[i];
                int nextValue = dp[j] + V[i];
                if (j != 0 && dp[j] == 0) {
                    continue;
                }

                if (nextSize <= m && nextValue > dp[nextSize]) {
                    dp[nextSize] = nextValue;
                    max = Math.max(max, nextValue);
                }
            }
        }
        return max;
    }
}
