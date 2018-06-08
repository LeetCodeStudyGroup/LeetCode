public class Solution {
    /**
     * @param nums: the array
     * @return: the minimum times to flip digit
     */
    public int flipDigit(int[] nums) {
        // Write your code here
        int n = nums.length;
        if (n == 0 || n == 1)
            return 0;

        int[] zero = new int[n + 1], one = new int[n + 1];
        for (int i = 0; i < n; i++) {
            one[i + 1] = one[i];
            if (nums[i] == 0) {
                one[i + 1]++;
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            zero[i] = zero[i + 1];
            if (nums[i] == 1) {
                zero[i]++;
            }
        }

        int result = zero[0];
        for (int i = 1; i < n; i++) {
            result = Math.min(result, one[i] + zero[i + 1]);
        }
        result = Math.min(result, one[n]);

        return result;
    }
}
