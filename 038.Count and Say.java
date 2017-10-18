/*
    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.
    Given an integer n, generate the nth term of the count-and-say sequence.

    Note: Each term of the sequence of integers will be represented as a string.

    Example 1:

    Input: 1
    Output: "1"
    Example 2:

    Input: 4
    Output: "1211"
     */

    public String countAndSay(int n) {
        String result = "1";

        if (n <= 1)
            return result;

        for (int i = n; i > 1; i --) {
            String temp = "";
            int count = 1;
            char current = result.charAt(0);
            for (int j = 1; j < result.length(); j++) {
                if (result.charAt(j) == current)
                    count++;
                else {
                    temp = temp + count + current;
                    count = 1;
                    current = result.charAt(j);
                }
            }
            result = temp + count + current;
        }

        return result;
    }
