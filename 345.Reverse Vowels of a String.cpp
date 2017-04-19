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

//====================== improve version =========================

class Solution {
public:
    string reverseVowels(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            i = s.find_first_of("aeiouAEIOU", i);
            j = s.find_last_of("aeiouAEIOU", j);
            if (i < j) {
                swap(s[i++], s[j--]);
            }
        }
        return s;
    }
};
