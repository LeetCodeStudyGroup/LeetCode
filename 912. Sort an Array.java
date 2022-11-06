/**
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
*/

class Solution {
    public int[] sortArray(int[] nums) {
        sort(nums, 0, nums.length - 1);
        return nums;
    }
    
    public static void sort(int[] number, int left, int right) {
        if(left < right) { 
            int s = number[(left+right)/2]; 
            int i = left - 1; 
            int j = right + 1; 

            while(true) {
                while(number[++i] < s) ;
                while(number[--j] > s) ; 
                if(i >= j) 
                    break; 
                swap(number, i, j); 
            } 

            sort(number, left, i-1);
            sort(number, j+1, right); 
        }
    }
    
    public static void swap(int[] number, int i, int j) {
        int t = number[i]; 
        number[i] = number[j]; 
        number[j] = t;
    }
}
