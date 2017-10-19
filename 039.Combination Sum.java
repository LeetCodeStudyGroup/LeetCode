/*
    Given a set of candidate numbers (C) (without duplicates) and a target number (T),
    find all unique combinations in C where the candidate numbers sums to T.

    The same repeated number may be chosen from C unlimited number of times.

    Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    For example, given candidate set [2, 3, 6, 7] and target 7,
    A solution set is:
    [
      [7],
      [2, 2, 3]
    ]
     */

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
        Arrays.sort(candidates);
        findSubset(list, candidates, target, new ArrayList<Integer>(), 0);
        return list;
    }

    public void findSubset(List<List<Integer>> list, int [] candidates, int remain, ArrayList<Integer> subset, int start) {
        if (remain < 0)
            return;
        else if (remain == 0)
            list.add(new ArrayList<>(subset));
        else {
            for (int i=start; i<candidates.length; i++) {
                subset.add(candidates[i]);
                findSubset(list, candidates, remain - candidates[i], subset, i); // not i + 1 because we can reuse same elements
                subset.remove(subset.size() - 1);
            }
        }
    }
