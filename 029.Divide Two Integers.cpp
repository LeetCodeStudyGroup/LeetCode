class Solution {
public:
    int divide(int dividend, int divisor) {
        bool negative = false;
        if (divisor == 0)
            return std::numeric_limits<int>::max();
        if (dividend < 0) {
            negative = !negative;
            if (dividend == -2147483648)
                dividend = 2147483647;
            else
                dividend = abs(dividend);
        }
        if (divisor < 0) {
            negative = !negative;
            divisor = abs(divisor);
        }
            
        int count = 0;
        while (dividend >= divisor) {
            count++;
            dividend -= divisor;
        }
        
        if (negative)
            count = 0 - count;
        
        return count;
    }
};
