public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        boolean[] dp = new boolean[m + 1];
        int max = 0;
        dp[0] = true;
        for (int i = 0; i < A.length; i++) {
            for (int j = m; j >= 0; j--) {
                if (dp[j] && (j + A[i] <= m)) {
                    dp[j + A[i]] = true;
                    max = Math.max(max, j + A[i]);
                }
            }
        }
        return max;
    }

}
