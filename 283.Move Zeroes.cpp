class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zeroIndex = 0;
        for (int i=0; i<nums.size(); i++) {
            if (nums[i] != 0) {
                nums[zeroIndex] = nums[i];
                zeroIndex++;
            } 
        }
        
        for (int i=zeroIndex; i<nums.size(); i++) {
            nums[i] = 0;
        }
    }
};
