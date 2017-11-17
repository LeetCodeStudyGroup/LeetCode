/*
    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Write a function to determine if a given target is in the array.

    The array may contain duplicates.
     */

    public boolean search(int[] nums, int target) {
        int low = 0, high = nums.length-1;
        if (high < 0)
            return false;
        int middle;
        while (low < high) {
            middle = (low + high) / 2;
            if (nums[middle] == target)
                return true;
            if (nums[low] < nums[middle]) {
                if (nums[middle] > target && nums[low] <= target)
                    high = middle;
                else
                    low = middle + 1;
            } else if (nums[middle] < nums[high]) {
                if (nums[middle] < target && nums[high] >= target)
                    low = middle + 1;
                else
                    high = middle;
            } else {
                if (nums[high] == target)
                    return true;
                else
                    high--;
            }
        }

        return nums[low] == target;
    }
