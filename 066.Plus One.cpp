class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int head = digits.size() - 1;
        if(digits.size() == 0)
            return digits;
            
        int flag = (digits[head] + 1) / 10;
        digits[head] = (digits[head] + 1) % 10;
        for (int i = head-1; i >= 0; i--) {
            int sum = flag + digits[i];
            digits[i] = sum % 10;
            flag = sum / 10;
        }
        
        if (flag != 0) {
            // vector<int>::iterator iterator = digits.begin();
            digits.insert(digits.begin(), flag);
        }
        
        return digits;
    }
};

// ============ improve ================

class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
    	for (int i = n - 1; i >= 0; --i)
    	{
    		if (digits[i] == 9)
    		{
    			digits[i] = 0;
    		}
    		else
    		{
    			digits[i]++;
    			return digits;
    		}
    	}
    	
    	digits[0] = 1;
    	digits.push_back(0);
        
        return digits;
    }
};
