/*
    Given a sorted array and a target value, return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

    Here are few examples.
    [1,3,5,6], 5 → 2
    [1,3,5,6], 2 → 1
    [1,3,5,6], 7 → 4
    [1,3,5,6], 0 → 0
     */

    public int searchInsert(int[] nums, int target) {
        if (nums.length == 0)
            return 0;

        return searchIndex(nums, target, 0, nums.length - 1);
    }

    public int searchIndex(int [] nums, int target, int begin, int end) {
        if (begin == end) {
            if (nums[begin] == target)
                return begin;
            if (target < nums[begin])
                return begin;
            if (target > nums[begin])
                return nums.length;
        }

        if (begin == end - 1) {
            if (nums[begin] >= target)
                return begin;
            if (nums[end] == target || (nums[begin] < target && nums[end] > target))
                return end;
            return nums.length;
        }

        int index = (begin + end) / 2;
        if (nums[index] == target)
            return index;

        return Math.min(searchIndex(nums, target, begin, index), searchIndex(nums, target, index + 1, end));
    }
