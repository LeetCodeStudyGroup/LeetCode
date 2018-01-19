/*
    Given a list of numbers that may has duplicate numbers, return all possible subsets

    Notice:
    Each element in a subset must be in non-descending order.
    The ordering between two subsets is free.
    The solution set must not contain duplicate subsets.

    Example
    If S = [1,2,2], a solution is:

    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
    */

    /*
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    /*
     * @param nums: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> results = new ArrayList<> ();
        if (nums == null)
            return results;

        if (nums.length == 0) {
            results.add(new ArrayList<Integer> ());
            return results;
        }

        Arrays.sort(nums);
        subsetHelper(nums, 0, new ArrayList<Integer>(), results);

        return results;
    }

    public void subsetHelper(int[] nums, int index, List<Integer> subset, List<List<Integer>> results) {
        results.add(new ArrayList<Integer>(subset));

        for (int i = index; i < nums.length; i++) {
            if (i > 0 && nums[i-1] == nums[i] && i != index)
                continue;
            subset.add(nums[i]);
            subsetHelper(nums, i + 1, subset, results);
            subset.remove(subset.size() - 1);
        }
    }
