class Solution {
    func canJump(_ nums: [Int]) -> Bool {
        
        if nums.count == 0 {
            return false
        }
        
        if nums.count == 1 {
            return true
        }
        
        var minTrue = nums.count - 1
        for index in stride(from: nums.count-1, through: 0, by: -1) {
            
            if index + nums[index] >= minTrue {
                minTrue = index
            }
        }
        
        return minTrue == 0
    }
}
