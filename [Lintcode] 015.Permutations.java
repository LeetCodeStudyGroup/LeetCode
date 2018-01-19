/*
    Given a list of numbers, return all possible permutations.

    You can assume that there is no duplicate numbers in the list.

    For nums = [1,2,3], the permutations are:

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
*/

    /*
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> results = new ArrayList<>();

        if (nums == null)
            return results;

        if (nums.length == 0) {
            results.add(new ArrayList<Integer>());
            return results;
        }

        Set<Integer> set = new HashSet<>();
        permuteHelper(nums, new ArrayList<Integer>(), set, results);

        return results;
    }

    public void permuteHelper(int[] nums, List<Integer> subsets, Set<Integer> hash, List<List<Integer>> results) {
        if (subsets.size() == nums.length) {
            results.add(new ArrayList<Integer>(subsets)); // 要new才不會重複
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (hash.contains(nums[i])) {
                continue;
            }

            subsets.add(nums[i]);
            hash.add(nums[i]);
            permuteHelper(nums, subsets, hash, results);
            subsets.remove(hash.size() - 1);
            hash.remove(nums[i]);
        }
    }
