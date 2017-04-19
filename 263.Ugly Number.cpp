class Solution {
public:
    bool isUgly(int num) {
        if (num <= 0)
            return false;
        if (num == 1)
            return true;
            
        if (num % 2 == 0 || num % 3 == 0 || num % 5 == 0) {
            if (getDivideNum(num) == 1)
                return true;
        }
            
        return false;
    }
    
    int getDivideNum(int num) {
        if (num == 1)
            return num;
            
        if (num % 2 == 0)
            return getDivideNum(num/2);
        if (num % 3 == 0)
            return getDivideNum(num/3);
        if (num % 5 == 0)
            return getDivideNum(num/5);
            
        return num;
    }
};

// ================= improve ====================

for (int i=2; i<6 && num; i++)
    while (num % i == 0)
        num /= i;
return num == 1;
