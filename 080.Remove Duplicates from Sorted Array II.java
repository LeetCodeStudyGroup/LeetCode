/*
    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?

    For example,
    Given sorted array nums = [1,1,1,2,2,3],

    Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
    It doesn't matter what you leave beyond the new length.
     */

    public int removeDuplicates(int[] nums) {
        Arrays.sort(nums);
        if (nums.length == 0)
            return 0;
        int count = 1;
        int same = 0;

        for (int i=1; i<nums.length; i++) {
            int index = count;
            if (nums[i-1] != nums[i]) {
                count++;
                same = 0;
            } else {
                same++;
                if (same < 2) {
                    count++;
                }
            }
            nums[index] = nums[i];
        }

        return count;
    }
