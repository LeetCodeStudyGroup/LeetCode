/*
 Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
  */

    public boolean isValid(String s) {
        ArrayList<Character> arrayList= new ArrayList<Character>();
        char[] charArray = s.toCharArray();
        for (int i = 0; i < charArray.length; i++) {
            int index = arrayList.size() - 1;
            if (index > -1 && arrayList.get(index) == charArray[i])
                arrayList.remove(index);
            else {
                if (charArray[i] == '(' || charArray[i] == '[' || charArray[i] == '{') {
                    if (charArray[i] == '(')
                        arrayList.add(')');
                    else if (charArray[i] == '[')
                        arrayList.add(']');
                    else if (charArray[i] == '{')
                        arrayList.add('}');
                } else {
                    return false;
                }
            }
        }

        return arrayList.size() == 0;
    }
