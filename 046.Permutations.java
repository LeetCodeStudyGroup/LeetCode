/*
    Given a collection of distinct numbers, return all possible permutations.

    For example,
    [1,2,3] have the following permutations:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
     */

    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> list = new ArrayList<>();
        backtrace(list, new ArrayList<Integer>(), nums);
        return list;
    }

    public void backtrace(List<List<Integer>> list, List<Integer> temp, int[] nums) {
        if (temp.size() == nums.length)
//            list.add(temp); >> is null
            list.add(new ArrayList<>(temp));
        else {
            for (int i=0; i<nums.length; i++) {
                if (!temp.contains(nums[i])) {
                    temp.add(nums[i]);
                    backtrace(list, temp, nums);
                    temp.remove(temp.size() - 1);
                }
            }
        }
    }
