/*
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:

    [
      [2,4],
      [3,4],
      [2,3],
      [1,2],
      [1,3],
      [1,4],
    ]
     */

    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<>();
        findCombine(result, new ArrayList<Integer>(),1, n, k);

        return result;
    }

    public void findCombine(List<List<Integer>> result, List<Integer> now, int start, int range, int count) {
        if (count == 0) {
            result.add(new ArrayList<Integer>(now));
        }

        for (int i=start; i<=range; i++) {
            now.add(i);
            findCombine(result, now, i+1, range, count-1);
            now.remove(now.size()-1);
        }
    }
