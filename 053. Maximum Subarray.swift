class Solution {
    var max = Int.min
    
    func maxSubArray(_ nums: [Int]) -> Int {
        if nums.count == 0 {
            return 0
        }
        
        var sum = 0
        max = nums.first!
        for i in 0 ..< nums.count {
            sum += nums[i]
            
            if sum > max {
                max = sum
            }
            
            if sum < 0 {
                sum = 0
            }
        }
        
        return max
    }
}
