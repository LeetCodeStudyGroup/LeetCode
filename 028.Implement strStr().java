/*
    Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
     */

    public int strStr(String haystack, String needle) {
        if (needle.isEmpty())
            return 0;
        for (int i=0; i<haystack.length(); i++) {
            int index = i;
            for (int j=0; j<needle.length(); j++) {
                if (haystack.length() - i < needle.length())
                    return -1;
                if (j == needle.length()-1 && haystack.charAt(index) == needle.charAt(j))
                    return i;
                if (haystack.charAt(index) != needle.charAt(j))
                    break;
                index++;
            }
        }

        return -1;
    }
