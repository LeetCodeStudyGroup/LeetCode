class Solution {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        return rangeBinarySearch(nums: nums, target: target)
    }
    

    func rangeBinarySearch(nums: [Int], target: Int) -> [Int] {
        
        let foundedIndex = binarySearch(nums: nums, target: target)
        
        if foundedIndex == -1 {
            return [-1, -1]
        }
        
        let rightIndex = rightRangeOfTarget(nums: nums, target: target, startIndex: foundedIndex, endIndex: nums.count-1 )
        let leftIndex = leftRangeOfTarget(nums: nums, target: target, startIndex: nums.startIndex, endIndex: foundedIndex)
        
        return [leftIndex, rightIndex]
    }
    
    func binarySearch(nums: [Int], target: Int) -> Int {
        
        guard nums.count != 0 else {
            return -1
        }
        
        var frontIndex = nums.startIndex
        var rearIndex = nums.count - 1
        
        while frontIndex <= rearIndex {
            let searchIndex = (frontIndex + rearIndex) / 2
            
            if nums[searchIndex] == target {
                return searchIndex
            } else if nums[searchIndex] < target {
                frontIndex = searchIndex + 1
            } else {
                rearIndex = searchIndex - 1
            }
        }
        
        return -1
    }
    
    
    
    func rightRangeOfTarget(nums: [Int], target: Int, startIndex: Int, endIndex: Int ) -> Int {
        guard nums.count != 0 else {
            return -1
        }
        
        var frontIndex = startIndex
        var rearIndex = endIndex
        var rightIndex = startIndex
        
        while frontIndex <= rearIndex {
            
            if nums[rearIndex] == target {
                return rearIndex
            }
            
            let searchIndex = (frontIndex + rearIndex) / 2
            
            if nums[searchIndex] == target {
                rightIndex = searchIndex
                frontIndex = searchIndex + 1    // need 找到target 的最右邊的 index
            } else {
                // target <= nums[searchIndex]
                
                rearIndex = searchIndex - 1
            }
        }
        
        return rightIndex
    }
    
    func leftRangeOfTarget(nums: [Int], target: Int, startIndex: Int, endIndex: Int ) -> Int {
        guard nums.count != 0 else {
            return -1
        }
        
        var frontIndex = startIndex
        var rearIndex = endIndex
        var leftIndex = endIndex
        
        while frontIndex <= rearIndex {
            
            if nums[startIndex] == target {
                return startIndex
            }
            
            let searchIndex = (frontIndex + rearIndex) / 2
            
            if nums[searchIndex] == target {
                leftIndex = searchIndex
                rearIndex = searchIndex - 1    // need 找到target 的最左邊的 index
            } else {
                // target >= nums[searchIndex]
                
                frontIndex = searchIndex + 1
            }
        }
        
        return leftIndex
    }
}
