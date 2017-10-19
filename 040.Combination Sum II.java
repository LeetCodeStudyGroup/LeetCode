/*
    Given a collection of candidate numbers (C) and a target number (T),
    find all unique combinations in C where the candidate numbers sums to T.

    Each number in C may only be used once in the combination.

    Note:
    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.
    For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
    A solution set is:
    [
      [1, 7],
      [1, 2, 5],
      [2, 6],
      [1, 1, 6]
    ]
     */

    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
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
                if(i > start && candidates[i] == candidates[i-1]) continue; // skip duplicates
                subset.add(candidates[i]);
                findSubset(list, candidates, remain - candidates[i], subset, i+1);
                subset.remove(subset.size() - 1);
            }
        }
    }
