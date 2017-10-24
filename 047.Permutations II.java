/*
    Given a collection of numbers that might contain duplicates, return all possible unique permutations.

    For example,
    [1,1,2] have the following unique permutations:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
     */

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<Integer>(), nums, new boolean[nums.length]);
        return list;
    }

    private void backtrack(List<List<Integer>> list, List<Integer> temp, int [] nums, boolean [] used) {
        if (temp.size() == nums.length) {
            list.add(new ArrayList<>(temp));
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]))
                    continue;
                else {
                    used[i] = true;
                    temp.add(nums[i]);
                    backtrack(list, temp, nums, used);
                    used[i] = false;
                    temp.remove(temp.size() - 1);
                }
            }
        }
    }
