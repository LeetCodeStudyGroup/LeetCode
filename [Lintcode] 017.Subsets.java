/*
    Given a set of distinct integers, return all possible subsets.
    Example
    If S = [1,2,3], a solution is:

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

    Notice:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.
    */

    /*
     * @param nums: A set of numbers
     * @return: A list of lists
     */
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null)
            return results;

        if (nums.length == 0) {
            results.add(new ArrayList<Integer>());
            return results;
        }

        Arrays.sort(nums);
        subsetsHelper(nums, 0, new ArrayList<Integer>(), results);

        return results;
    }

    public void subsetsHelper(int[] nums, int index, List<Integer> subset, List<List<Integer>> results) {
        results.add(new ArrayList<Integer>(subset)); // avoid change

        for (int i = index; i < nums.length; i++) {
            subset.add(nums[i]);
            subsetsHelper(nums, i + 1, subset, results);
            subset.remove(subset.size() - 1);
        }
    }
