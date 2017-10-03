/*
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    For "(()", the longest valid parentheses substring is "()", which has length = 2.

    Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
     */

    int longestValidParentheses(String s) {
        int n = s.length();
        int longest = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '(') stack.push(i);
            else {
                if (!stack.isEmpty()) {
                    if (s.charAt(stack.peek()) == '(') stack.pop();
                    else stack.push(i);
                }
                else stack.push(i);
            }
        }
        if (stack.isEmpty()) longest = n;
        else {
            int a = n, b = 0;
            while (!stack.isEmpty()) {
                b = stack.peek(); stack.pop();
                longest = Math.max(longest, a-b-1);
                a = b;
            }
            longest = Math.max(longest, a);
        }
        return longest;
    }
