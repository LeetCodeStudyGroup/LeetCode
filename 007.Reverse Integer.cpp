public class Solution {
    public int reverse(int x) {
        long result = 0;
        while (x != 0) {
            result = result * 10 + x % 10;
            
            if(result > Integer.MAX_VALUE || result < Integer.MIN_VALUE) {
                return 0;
            }
        
            x /= 10;
        }
        
        return (int)result;
    }
}

//====================================================

class Solution {
public:
    int reverse(int x) {
        int index = 0;
        stringstream ss;
        ss << x;
        string str = ss.str();
        string result = "";
        if (str[0] == '-') {
            result = "-";
            index++;
        }
        for (int i = str.size() - 1; i >= index; i--) {
            result += str[i];
        }
        int iResult;
        istringstream ( result ) >> iResult;
        
        if(iResult == 2147483647 || iResult == -2147483648) {
            // integer 32 bit overflow positive is equal to 2147483647 and negative is equal to -2147483648
            // if overflow, return result == 0
            return 0;
        }
            
        return iResult;
    }
};
