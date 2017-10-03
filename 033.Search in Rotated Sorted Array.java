/*
    Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.
     */

    public int search(int[] nums, int target) {
        if (nums.length == 0)
            return -1;
        if (nums.length == 1) {
            if (nums[0] == target)
                return 0;
            else
                return -1;
        }

        int left = searchByBinary(nums, 0, nums.length/2 - 1, target);
        int right = searchByBinary(nums, nums.length/2, nums.length - 1, target);

        if (left != -1)
            return left;

        return right;
    }

    public int searchByBinary (int[] nums, int left, int right, int target) {
        if (left == right) {
            if (nums[left] == target)
                return left;
            else
                return -1;
        }

        int middle = (left + right) / 2;

        if (nums[left] > nums[right]) {
            int leftIndex = searchByBinary(nums, left, middle, target);
            int rightIndex = searchByBinary(nums, middle + 1, right, target);
            return leftIndex == -1 ? rightIndex : leftIndex;
        }

        if (nums[middle] == target)
            return middle;
        if (nums[middle] > target)
            return searchByBinary(nums, left, middle, target);
        return searchByBinary(nums, middle + 1, right, target);
    }
