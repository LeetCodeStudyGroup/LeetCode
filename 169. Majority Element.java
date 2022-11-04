/**
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
*/

class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> hash = new HashMap<Integer,Integer>();
        int count = nums.length / 2 + 1;
        
        for (int i=0; i<nums.length; i++) {
            if (!hash.containsKey(nums[i]))
                hash.put(nums[i], 1);
            else 
                hash.put(nums[i], hash.get(nums[i]) + 1);
            if (hash.get(nums[i]) == count)
                return nums[i];
                
        }
        return 0;
    }
}
