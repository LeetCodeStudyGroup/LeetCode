class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.size() <= 1)
            return s.size();

        map<char, int> substringList;
        int beginIndex = 0;
        int maxResult = 0;
        substringList.insert(pair<char, int>(s[0], 0));
        for (int i = 1; i < s.size(); i++) {
            map<char, int>::iterator iter = substringList.find(s[i]);
            if ((iter->second >= beginIndex) && (iter != substringList.end())) {
                if (i - beginIndex > maxResult) {
                    maxResult = i - beginIndex;
                }
                beginIndex = iter->second + 1;
            }
            substringList[s[i]] = i;
        }
        if (s.size() - beginIndex > maxResult) {
            maxResult = s.size() - beginIndex;
        }

        return maxResult;
    }
};
