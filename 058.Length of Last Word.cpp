public class Solution {
    public int lengthOfLastWord(String s) {
        int totalLength =  s.trim().length(); //去掉頭尾空白的長度
        int LastSpaceIndex = s.trim().lastIndexOf(" ");
        
        
        return totalLength - LastSpaceIndex - 1;
    }
}
//==========================================================
class Solution {
public:
    vector<string> split(const string &s, char delim) {
        vector<string> elems;
        stringstream ss;
        ss.str(s);
        string item;
        while (getline(ss, item, delim)) {
            elems.push_back(item);
        }
        
        return elems;
    }
    
    int lengthOfLastWord(string s) {
        string result;
        vector<string> splitStr = split(s, ' ');
        
        for(int i=splitStr.size()-1; i >= 0; i--) {
            if(!splitStr[i].empty()) {
                result = splitStr[i];
                break;
            }
        }
        
        if(splitStr.size() == 0)
            return 0;
        
        return result.size();
    }
};
