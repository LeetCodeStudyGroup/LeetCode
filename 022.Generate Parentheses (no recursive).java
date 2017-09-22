/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/

// use loop

    public List<String> generateParenthesis(int n) {
        List<String> result = new LinkedList<>();
        List<Integer> diff = new LinkedList<>();

        if (n <= 0)
            return result;

        result.add("");
        diff.add(0);

        for (int i=0; i<2*n; i++) {
            List<String> temp_result = new LinkedList<>();
            List<Integer> temp_diff = new LinkedList<>();

            for (int j=0; j<result.size(); j++) {
                String result_previous = result.get(j);
                int diff_previous = diff.get(j);

                if (i < 2 * n - 1 && diff.get(j) + i < 2*n) {
                    temp_result.add(result_previous + "(");
                    temp_diff.add(diff_previous + 1);
                }

                if (i < 2 * n && diff.get(j) > 0) {
                    temp_result.add(result_previous + ")");
                    temp_diff.add(diff_previous - 1);
                }
            }

            result = new ArrayList<>(temp_result);
            diff = new ArrayList<>(temp_diff);
        }

        return result;
    }
