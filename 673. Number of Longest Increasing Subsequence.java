/**
     * 673. Number of Longest Increasing Subsequence
     * Medium
     * 4.4K
     * 196
     * Companies
     * Given an integer array nums, return the number of longest increasing subsequences.
     *
     * Notice that the sequence has to be strictly increasing.
     *
     *
     *
     * Example 1:
     *
     * Input: nums = [1,3,5,4,7]
     * Output: 2
     * Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
     * Example 2:
     *
     * Input: nums = [2,2,2,2,2]
     * Output: 5
     * Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
     *
     *
     * Constraints:
     *
     * 1 <= nums.length <= 2000
     * -106 <= nums[i] <= 106
     */

//    public int findNumberOfLIS(int[] nums) {
//
//    }
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length, res = 0, max_len = 0;
        int[] len = new int[n];
        int[] cnt = new int[n];
        for (int i = 0; i<n; i++) {
            len[i] = cnt[i] = 1;
            for (int j = 0; j < i ; j++) {
                if (nums[j] < nums[i]) {
                    if (len[i] == len[j] + 1)
                        cnt[i] += cnt[j];
                    if (len[i] < len[j] + 1) {
                        len[i] = len[j] + 1;
                        cnt[i] = cnt[j];
                    }
                }
            }
            if (max_len == len[i])
                res += cnt[i];
            if (max_len < len[i]) {
                max_len = len[i];
                res = cnt[i];
            }
        }
        return res;
    }
