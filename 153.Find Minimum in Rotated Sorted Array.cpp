class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums.size() == 0)
            return -1;
        if (nums.size() == 1)
            return 1;
            
        for (int i=1; i<nums.size(); i++) {
            if (nums[i-1] > nums[i])
                return nums[i];
        }
        
        return nums[0];
    }
};
