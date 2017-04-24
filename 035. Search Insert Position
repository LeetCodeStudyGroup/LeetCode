class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {
        
        if nums.count == 0 {
            return 0
        }
        
        var frontIndex = nums.startIndex
        var rearIndex = nums.startIndex + nums.count - 1
        var searchIndex = 0
        
        while frontIndex <= rearIndex {
            
            searchIndex = (rearIndex + frontIndex) / 2
            
            if nums[searchIndex] == target {
                return searchIndex
                
            } else if nums[searchIndex] < target {
                frontIndex = searchIndex + 1
            
            } else if nums[searchIndex] > target{
                rearIndex = searchIndex - 1
            }
        }
    
        for (index, value) in nums.enumerated() {
            if target < value  {
                return index
            }
        }
        
        return nums.endIndex
    }
}
