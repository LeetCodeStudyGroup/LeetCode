class Solution {
    func findMin(_ nums: [Int]) -> Int {
        guard nums.count > 0 else {
            return Int.min
        }
        
        var left = nums.startIndex
        var right = nums.endIndex - 1
        
        if nums.count == 1 {
            return nums[nums.startIndex]
        }
        
        while left < right {
            
            if nums[left] < nums[right] {
                return nums[left]
            }
            
            let mid = (left + right) / 2
            
            if nums[mid] >= nums[nums.startIndex] {
                left = mid + 1
                
            } else if nums[mid] < nums[nums.startIndex] {
                right = mid
            }
        }
        
        return nums[left]
    }
}
