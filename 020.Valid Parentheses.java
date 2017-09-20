/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

*/

    public boolean isValid(String s) {
        if (s.isEmpty())
            return true;
        Stack stack = new Stack();

        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '(' || s.charAt(i) == '{' || s.charAt(i) == '[')
                stack.push(s.charAt(i));
            else if (s.charAt(i) == ')') {
                if (stack.isEmpty() || (char) stack.pop() != '(')
                    return false;
            } else if (s.charAt(i) == '}') {
                if (stack.isEmpty() || (char) stack.pop() != '{')
                    return false;
            } else if (s.charAt(i) == ']') {
                if (stack.isEmpty() || (char) stack.pop() != '[')
                    return false;
            } else {

            }
        }

        if (stack.isEmpty())
            return true;

        return false;
    }
