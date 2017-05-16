class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        
        if (nums.size() < 3)
            return result;
            
        sort(nums.begin(), nums.end());
        // test case [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6] 
        for (int c = nums.size() - 1; c > 1; c--) {
            int a = 0;
            int b = c - 1;
            while (a < b) {
                int sum = nums[a] + nums[b];
                if (sum == - nums[c]) {
                    vector<int> temp;
                    temp.push_back(nums[a]);
                    temp.push_back(nums[b]);
                    temp.push_back(nums[c]);
                    result.push_back(temp);
                    a++;b--;
                    while (a < b && nums[a] == nums[a-1])
                        a++;
                    while (a < b && nums[b] == nums[b+1])
                        b--;
                } else if (sum > - nums[c]) {
                    b--;
                } else {
                    a++;
                }
            }
            while (c > 1 && nums[c] == nums[c-1]) {
                // remove duplicate value
                c--;
            }
        }
        
        return result;
    }
};
