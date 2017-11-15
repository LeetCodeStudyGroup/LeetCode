/*
    Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
    with the colors in the order red, white and blue.

    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

    Note:
    You are not suppose to use the library's sort function for this problem.

    click to show follow up.
     */

    public void sortColors(int[] nums) {
        for (int i=0; i<nums.length; i++) {
            for (int j=1; j<nums.length; j++) {
                if (nums[i] > nums[j] && i<j) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                }
            }
        }
    }
