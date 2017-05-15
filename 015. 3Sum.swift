class Solution {
    func threeSum(_ nums: [Int]) -> [[Int]] {
        
        if nums.count < 3 {
            return []
        }
        
        let sortedNums = nums.sorted()
        
        var results = [[Int]]()
        
        for i in 0 ..< sortedNums.count - 2 {
            
            if i > 0 && sortedNums[i] == sortedNums[i-1] {
                continue
            }
            
            let target = -sortedNums[i]
            
            if let twoSum = findTwoSum(sortedNums, i + 1, target) {
                for result in twoSum {
                    var solution = result
                    solution.append(sortedNums[i])
                    results.append(solution)
                }
            }
        }
        
        return results
    }
    
    private func findTwoSum(_ nums: [Int], _ startIndex: Int, _ target: Int) -> [[Int]]? {
        
        if nums.count < 2 {
            return nil
        }
        
        var results = [[Int]]()
        
        var left = startIndex
        var right = nums.endIndex - 1
        
        while left < right {
            if nums[left] + nums[right] == target {
                results.append([nums[left], nums[right]])
                
                left += 1
                while left < right && nums[left] == nums[left - 1] {
                    left += 1
                }
                
                right -= 1
                while left < right && nums[right] == nums[right + 1] {
                    right -= 1
                }
                
            } else if nums[left] + nums[right] > target {
                right -= 1
            } else if nums[left] + nums[right] < target{
                left += 1
            }
        }
        
        return results
    }
}
