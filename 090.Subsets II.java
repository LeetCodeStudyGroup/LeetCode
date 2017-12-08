/*
    Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

    Note: The solution set must not contain duplicate subsets.

    For example,
    If nums = [1,2,2], a solution is:

    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
     */

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<Integer>());
        if (nums.length == 0)
            return result;
        Arrays.sort(nums);
        int size = 0, startIndex = 0;
        for (int i=startIndex; i<nums.length; i++) {
            startIndex = (i > 0 &&  nums[i-1] == nums[i])? size : 0;
            size = result.size();
            for (int j=startIndex; j<size; j++) {
                List temp = new ArrayList(result.get(j));
                temp.add(nums[i]);
                result.add(temp);
            }
        }

        return result;
    }
