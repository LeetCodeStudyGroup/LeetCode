/*
    For a given source string and a target string, you should output the first index(from 0)
    of target string in source string.

    If target does not exist in source, just return -1.

    Example
    If source = "source" and target = "target", return -1.

    If source = "abcdabcdefg" and target = "bcd", return 1.
    */

    /*
     * @param source: source string to be scanned.
     * @param target: target string containing the sequence of characters to match
     * @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
     */
    public int strStr(String source, String target) {
        if (source == null || target == null) {
            return -1;
        }

        for (int i = 0; i < source.length() - target.length() + 1; i++) {
            int j = 0;
            for (; j < target.length(); j++) {
                if (source.charAt(i + j) != target.charAt(j))
                    break;
            }
            if (j == target.length())
                return i;
        }

        return -1;
    }
