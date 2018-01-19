  /*
    Given a list of numbers with duplicate number in it. Find all unique permutations.

    Example
    For numbers [1,2,2] the unique permutations are:

    [
      [1,2,2],
      [2,1,2],
      [2,2,1]
    ]
    */

    /*
     * @param :  A list of integers
     * @return: A list of unique permutations
     */
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();
        if (nums == null)
            return results;
        if (nums.length == 0) {
            results.add(new ArrayList<Integer>());
            return results;
        }

        Set<Integer> set = new HashSet<>();
        Arrays.sort(nums);
        permuteUniqueHelper(nums, set, new ArrayList<Integer>(), results);

        return results;
    }

    public void permuteUniqueHelper(int[] nums, Set<Integer> set, List<Integer> subset, List<List<Integer>> results) {
        if (nums.length == subset.size()) {
            results.add(new ArrayList<>(subset));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (set.contains(i) || (i > 0 && nums[i-1] == nums[i] && !set.contains(i-1)))
                continue;

            subset.add(nums[i]);
            set.add(i);
            permuteUniqueHelper(nums, set, subset, results);
            subset.remove(subset.size() - 1);
            set.remove(i);
        }
    }
