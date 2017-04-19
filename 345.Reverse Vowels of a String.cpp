class Solution {
public:
    string reverseVowels(string s) {
        vector<int> vowels;
        
        for (int i=0; i<s.length(); i++) {
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u'
                || s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U') {
                    vowels.push_back(i);
            }
        }
        
        int size = vowels.size();
        for (int i=0; i<size/2; i++) {
            char tmp = s[vowels[size-1-i]];
            s[vowels[size-1-i]] = s[vowels[i]];
            s[vowels[i]] = tmp;
        }
        
        return s;
    }
};
