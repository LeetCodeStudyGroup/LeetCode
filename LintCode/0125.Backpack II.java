public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @param V: Given n items with value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int[] V) {
        // write your code here
        int n = A.length;
        int[] dp = new int[m + 1];
        int max = 0;

        for (int i = 0; i < n; i++) {
            for (int j = m; j >= 0; j--) {
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
