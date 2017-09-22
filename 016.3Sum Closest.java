/*
    Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
    Return the sum of the three integers. You may assume that each input would have exactly one solution.

        For example, given array S = {-1 2 1 -4}, and target = 1.

        The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
    */
   
    public int threeSumClosest(int[] nums, int target) {
        int result = target > 0 ? Integer.MAX_VALUE : Integer.MAX_VALUE + target;
        Arrays.sort(nums);

        for (int i=0; i<nums.length-2; i++) {
            int low = i+1;
            int high = nums.length-1;
            while (low < high) {
                int temp = nums[low] + nums[i] + nums[high] - target;
                if (Math.abs(temp) < Math.abs(result - target))
                    result = nums[low] + nums[i] + nums[high];

                if (temp == 0)
                    return result;
                else if (temp < 0)
                    low++;
                else
                    high--;
            }
        }

        return result;
    }
