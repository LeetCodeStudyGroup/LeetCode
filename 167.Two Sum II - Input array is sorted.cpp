class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> result;
        
        if (numbers.size() == 0) {
            result.push_back(0);
            result.push_back(0);
            return result;
        }
        
        int index1 = 0;
        int index2 = numbers.size() - 1;
        
        while (index1 < index2) {
            int sum = numbers[index1] + numbers[index2];
            if (sum == target) {
                result.push_back(index1+1);
                result.push_back(index2+1);
                
                return result;
            } else if (sum < target) {
                index2--;
            } else {
                index1++;
            }
        }
        
        if (index1 >= index2) {
            result.push_back(0);
            result.push_back(0);
        }
        
        return result;
    }
};
