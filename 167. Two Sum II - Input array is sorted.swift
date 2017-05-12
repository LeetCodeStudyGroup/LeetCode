class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
        
        if nums.count <= 0 {
            return []
        }
        
        var left = nums.startIndex
        var right = nums.endIndex - 1
        
        while left <= right {
            
            if nums[left] + nums[right] == target {
                return [left+1, right+1]
            }
            
            if nums[left] + nums[right] > target {
                right -= 1
                continue
            }
            
            if nums[left] + nums[right] < target {
                left += 1
                continue
            }
        }
        
        return []
    }
}
