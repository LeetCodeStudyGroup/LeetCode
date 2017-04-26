class Solution {
    func findPeakElement(_ nums: [Int]) -> Int {
        guard nums.count > 0 else {
            return -1
        }
        
        if nums.count == 1 {
            return 0
        }
        
        var left = nums.startIndex
        var right = nums.endIndex - 1
        
        while left < right {
            let mid = left + (right - left) / 2
            
            if nums[mid] < nums[mid+1] {
                left = mid + 1
            } else if nums[mid] > nums[mid+1] {
                right = mid
            }
        }
        
        return left
    }
}
