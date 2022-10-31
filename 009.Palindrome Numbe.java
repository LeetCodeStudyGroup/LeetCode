import java.util.Vector;

/*

Determine whether an integer is a palindrome. Do this without extra space.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
*/

// Solution 1
    public boolean isPalindrome(int x) {
        Vector<Integer> vector = new Vector<>();
        if (x < 0)
            return false;

        x = Math.abs(x);
        while (x > 0) {
            vector.add(x % 10);
            x = x / 10;
        }

        int vectorSize = vector.size();
        for (int i=0; i<vectorSize/2; i++) {
            if (vector.get(i) != vector.get(vectorSize-i-1))
                return false;
        }

        return true;
    }

// Solution 2
    boolean isPalindrome(int x) {
        if (x < 0) return false;
        String s = Integer.toString(x);
        int begin = 0;
        int end = s.length() - 1;
        while (begin <= end) {
            if (s.charAt(begin) == s.charAt(end)) {
                begin++;
                end--;
            } else {
                return false;
            }
        }

        return true;
    }
