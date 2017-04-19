class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        unordered_set<int> tmp(nums1.begin(), nums1.end());
        if (nums1.empty() || nums2.empty())
            return result;
        
        for (int i: nums2) {
            if (tmp.count(i)) {
                result.push_back(i);
                tmp.erase(i);
            }
        }
        
        return result;
    }
};
