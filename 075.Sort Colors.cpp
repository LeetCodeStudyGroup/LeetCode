class Solution {
public:
    void sortColors(vector<int>& nums) {
        if (nums.size() < 2)
            return;
        
        int colorLeft = 0;
        int colorRight = nums.size() - 1;
        int i = 0;
        
        while (i <= colorRight) {
            if (nums[i] == 0) {
                swap(nums[colorLeft], nums[i]);
                colorLeft++;
                i++;
            } else if (nums[i] == 1) {
                i++;
            } else {
                swap(nums[colorRight], nums[i]);
                colorRight--;
            }
        }
    }
};
