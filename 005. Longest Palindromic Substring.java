public class Solution {
/*
    Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

    Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    Example:

    Input: "cbbd"

    Output: "bb"
 */
int index, length;

    public String longestPalindrome(String s) {
        if (s.length() < 2)
            return s;

        for (int i=0; i<s.length(); i++) {
            findPalindrome(i, i, s);
            findPalindrome(i, i + 1, s);
        }

        return s.substring(index, index + length);
    }

    private void findPalindrome(int index1, int index2, String s) {
        while (index1 >= 0 && index2 < s.length() && s.charAt(index1) == s.charAt(index2)) {
            index1--;
            index2++;
        }

        int currentLength = index2 - index1 - 1;
        if (currentLength > length) {
            length = currentLength;
            index = index1 + 1;
        }
    }
}
