class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.size() == 0)
            return -1;
        int low = 0;
        int high = nums.size()-1;
        while (low < high) {
            int index = (low + high) / 2;
            if (nums[index] == target) {
                return index;
            }
            
            if (nums[low] < nums[index]) {
                if (target < nums[index] && target >= nums[low]) {
                    high = index-1;
                } else {
                    low = index+1;
                }
            }
            if (nums[high] > nums[index]) {
                if (target > nums[index] && target <= nums[high]) {
                    low = index+1;
                } else {
                    high = index-1;
                }
            }
        }
        
        return (low <= high)? (low + high) / 2 : -1;
    }
};
