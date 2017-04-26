class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result;
        result.push_back(-1);
        result.push_back(-1);
        
        // search left index
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            int index = (left + right) / 2;
            if (nums[index] < target) {
                left = index+1;
            } else {
                right = index;
            }
        }
        
        if (left >= nums.size() || nums[left] != target)
            return result;
        result[0] = left;
            
        // search right index
        right = nums.size() - 1;
        while (left < right) {
            // if no add 1, it's may always in loop
            int index = (left + right) / 2 + 1;
            if (nums[index] > target) {
                right = index-1;
            } else {
                left = index;
            }
        }
        
        result[1] = right;
        
        return result;
    }
};
