class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        
        sort(nums.begin(), nums.end());
        
        int index = 1;
        int currentIndex = 1;
        int repeatNum = nums[0];
        int count = 1;
        
        for (currentIndex = 1; currentIndex < nums.size(); currentIndex++) {
            if (nums[currentIndex] == repeatNum) {
                if (count++ < 2) {
                    nums[index] = nums[currentIndex];
                    index++;
                }
            } else {
                count = 1;
                nums[index] = nums[currentIndex];
                repeatNum = nums[currentIndex];
                index++;
                
            }
        }
        
        return index;
    }
};
