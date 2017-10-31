/*
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a character sequence consists of non-space characters only.

    For example,
    Given s = "Hello World",
    return 5.
     */

    public int lengthOfLastWord(String s) {
        String[] strArray = s.split(" ");
        int size = strArray.length;
        if (size == 0)
            return 0;
        return strArray[size - 1].length();
    }
