class Solution {
public:

    int factorial(int n)
    {
        if(n == 1)
            return 1;
        else
            return n * factorial(n - 1) ;
    }
    
    int climbStairs(int n) {
        cout << n << endl;
        int count = 1;
        if(n == 0)
            return 0;
            
        int twoMax = n / 2;
        
        // cout << "twoMax = " << twoMax << endl;
        for(int i=1; i<=twoMax; i++) {
            int totalSize = n - i;
            // C totalSize get i
            // cout << "totalSize = " << totalSize << ", i = " << i << endl;
            count += factorial(totalSize) / (factorial(i) * factorial(totalSize - i));
            // cout << count << endl;
        }
        
        return count; 
    }
};

// ============= improve =================
class Solution {
public:
    int climbStairs(int n) {
        if(n == 0 || n == 1 || n == 2) {
            return n;
        }
        vector<int> mem(n,0);
        mem[0] = 1;
        mem[1] = 2;
        for(int i = 2; i < n; i++) {
            // cout << mem[i] << ", " << mem[i-1] << ", " << mem[i-2] << endl;
            mem[i] = mem[i-1] + mem[i-2];
        }
        return mem[n-1];
    }
};
