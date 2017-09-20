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

    List<String> result = new ArrayList<>();

    public List<String> generateParenthesis(int n) {
        if (n > 0)
            generateString("", n, n);

        return result;
    }

    public void generateString(String current, int countL, int countR) {
        if (countL == 0 && countR == 0)
            result.add(current);

        if (countL > 0)
            generateString(current + "(", countL-1, countR);
        if (countL < countR && countR > 0) {
            generateString(current + ")", countL, countR-1);
        }
    }
