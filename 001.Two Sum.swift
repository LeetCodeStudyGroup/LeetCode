class Solution {
    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    
        for i in 0..<nums.count {
            for j in i+1..<nums.count{
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
    
        return []
    }
}
