class Solution {
    // Approach #1 (Brute Force)
    func twoSum_1(_ nums: [Int], _ target: Int) -> [Int] {
        for i in 0..<nums.count {
            for j in i+1..<nums.count{
                if nums[i] + nums[j] == target {
                    return [i, j]
                }
            }
        }
        
        return []
    }
    
    // Approach #2 (Two-pass Hash Table)
    func twoSum_2(_ nums: [Int], _ target: Int) -> [Int] {
        var map = Dictionary<Int, Int>()
        
        for (index, num) in nums.enumerated() {
            map[num] = index
        }
   
        for (index, num) in nums.enumerated() {
            let complement = target - num
            if map[complement] != nil && map[complement] != index {
                    return [index, map[complement]!]
            }
        }
        
        return []
    }
    
    // Approach #3 (One-pass Hash Table)
    func twoSum_3(_ nums: [Int], _ target: Int) -> [Int] {
        var map = Dictionary<Int, Int>()

        for (index, num) in nums.enumerated() {
            let complement = target - num
            if map[complement] != nil && map[complement] != index {
                return [index, map[complement]!]
            }
            map[num] = index
        }
        
        return []
    }
}
