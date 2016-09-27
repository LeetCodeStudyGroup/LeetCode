class Solution {
public:
    string convert(string s, int numRows) {
        vector<vector<char> > tmp;
        bool increase = true;
        int index = 0;
        
        if(numRows == 1)
            return s;
        
        for (int i = 0; i < numRows; i++) {
            tmp.push_back(vector<char>());
        }
        
        for (int i = 0; i < s.length(); i++) {
            tmp[index].push_back(s[i]);
            if (increase) {
                if(index < numRows-1)
                    index++;
                else {
                    increase = !increase;
                    index--;
                }
            } else {
                if (index > 0)
                    index--;
                else {
                    increase = !increase;
                    index++;
                }
            }
        }
        
        string result = "";
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < tmp[i].size(); j++) {
                result += tmp[i][j];
            }
        }
        
        return result;
    }
};
