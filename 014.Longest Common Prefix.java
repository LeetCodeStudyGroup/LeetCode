/*
Write a function to find the longest common prefix string amongst an array of strings.
*/

    public String longestCommonPrefix(String[] strs) {
        String longestStr = "";

        if (strs.length == 0)
            return longestStr;
        else
            longestStr = strs[0];

        for (int i=1; i<strs.length; i++) {
            int j=0;
            for (;j<strs[i].length() && j<longestStr.length();j++) {
                if (strs[i].charAt(j) != longestStr.charAt(j))
                    break;
            }
            longestStr = longestStr.substring(0, j);
        }

        return longestStr;
    }
