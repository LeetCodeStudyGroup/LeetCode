class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.size() <= 1 || nums[0] > nums[1])
            return 0;
            
        for (int i=1; i<nums.size()-1; i++) {
            if (nums[i-1] < nums[i] && nums[i] > nums[i+1])
                return i;
        }
        
        return nums.size()-1;
    }
};
