/**
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
*/

class Solution {
    List<String> result = new ArrayList<String>();
    public List<String> letterCombinations(String digits) {
        if (digits == "")
            return null;
        
        for (int i=0; i<digits.length(); i++) {
            List<String> temp = new ArrayList<String>();
            if (i == 0)
                result.add("");
            for(int j=0; j<result.size(); j++) {
                String s = result.get(j);
                switch(digits.charAt(i)) {
                    case '2':
                        temp.add(s + "a");
                        temp.add(s + "b");
                        temp.add(s + "c");
                        break;
                    case '3':
                        temp.add(s + "d");
                        temp.add(s + "e");
                        temp.add(s + "f");
                        break;
                    case '4':
                        temp.add(s + "g");
                        temp.add(s + "h");
                        temp.add(s + "i");
                        break;
                    case '5':
                        temp.add(s + "j");
                        temp.add(s + "k");
                        temp.add(s + "l");
                        break;
                    case '6':
                        temp.add(s + "m");
                        temp.add(s + "n");
                        temp.add(s + "o");
                        break;
                    case '7':
                        temp.add(s + "p");
                        temp.add(s + "q");
                        temp.add(s + "r");
                        temp.add(s + "s");
                        break;
                    case '8':
                        temp.add(s + "t");
                        temp.add(s + "u");
                        temp.add(s + "v");
                        break;
                    case '9':
                        temp.add(s + "w");
                        temp.add(s + "x");
                        temp.add(s + "y");
                        temp.add(s + "z");
                        break;
                }
            }
            result = temp;
        }
        return result;
    }
}
