/*
    Given a string, find the length of the longest substring without repeating characters.

    Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
 */

    public int lengthOfLongestSubstring(String s) {
        if (s.length() <= 1)
            return s.length();
        int count = 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int previousSameCharIndex = 0;
        for (int i=0; i<s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                previousSameCharIndex = Math.max(previousSameCharIndex, map.get(s.charAt(i)) + 1);
            }

            count = Math.max (count, i - previousSameCharIndex + 1);
            map.put(s.charAt(i), i);
        }

        return count;
    }
