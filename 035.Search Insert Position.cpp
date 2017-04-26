class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
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
        
        if(nums[left] >= target)
            return left;
            
        return nums.size();
    }
};
