/*
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
 Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
*/

    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new LinkedList<>();

        if (nums.length < 4)
            return result;
        Arrays.sort(nums);

        for (int i=0; i<nums.length-3; i++) {
            while (i > 0 && nums[i] == nums[i-1] && i<nums.length-1) i++; // without repeat , but include [0,0,0,0] case
            int temp = target - nums[i];
            for (int j=i+1; j<nums.length-2; j++) {
                while (j-1 != i && nums[j] == nums[j-1] && j<nums.length-1) j++; // without repeat , but include [0,0,0,0] case
                int temp2 = temp - nums[j];
                int low = j+1;
                int high = nums.length - 1;
                while (low < high) {
                    if (nums[low] + nums[high] == temp2) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[low], nums[high]));
                        while (low < high && nums[low] == nums[low+1]) low++;
                        while (low < high && nums[high] == nums[high-1]) high--;
                        low++; high--;
                    } else if (nums[low] + nums[high] < temp2) {
                        low++;
                    } else {
                        high--;
                    }
                }
            }
        }

        return result;
    }
