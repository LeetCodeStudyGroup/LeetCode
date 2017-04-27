class Solution {
public:
    int divide(int dividend, int divisor) {
        if (divisor == 0 || (divisor == -1 && dividend == INT_MIN))
            return INT_MAX;
        
        bool negative = false;
        
        long long longDividend;
        long long longDivisor;
        if (dividend < 0) {
            negative = !negative;
            longDividend = abs((long long)dividend);
        } else {
            longDividend = dividend;
        }
        
        if (divisor < 0) {
            negative = !negative;
            longDivisor = abs((long long) divisor);
        } else {
            longDivisor = divisor;
        }
            
        int result = 0;
        while (longDividend >= longDivisor) {
            long long multiple = 1;
            long long divTmp = longDivisor;
            while (longDividend > divTmp << 1) {
                divTmp = divTmp << 1;
                multiple = multiple << 1;
            }
            result += multiple;
            longDividend -= divTmp;
        }
        
        return negative? -result : result;
    }
};
==================== Time out version =========================
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
