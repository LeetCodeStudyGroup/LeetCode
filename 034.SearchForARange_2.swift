class Solution_2 {
    func searchRange(_ nums: [Int], _ target: Int) -> [Int] {
        
        let startRange = findFirstPosition(nums, target)
        let endRange = findLastPosition(nums, target)
        
        return [startRange, endRange]
    }
    
    func findFirstPosition(_ nums: [Int], _ target: Int) -> Int {
        if nums.count == 0 {
            return -1
        }
        
        var start = nums.startIndex
        var end = nums.endIndex - 1
        
        while start < end {
            let mid = start + (end - start) / 2
            
            if nums[mid] == target {
                end = mid
            } else if nums[mid] < target {
                start = mid + 1
            } else if nums[mid] > target {
                end = mid - 1
            }
        }
        
        if nums[start] != target {
            return -1
        }
        
        return start
    }
    
    func findLastPosition(_ nums: [Int], _ target: Int) -> Int {
        if nums.count == 0 {
            return -1
        }
        
        var start = nums.startIndex
        var end = nums.endIndex - 1
        
        while start < end {
            let mid = start + (end - start) / 2
            
            if nums[mid] == target {
                start = mid
                
                if mid + 1 < nums.count && nums[mid+1] == target {
                    start = mid + 1
                }
                
                if mid + 1 < nums.count && nums[mid+1] != target {
                    end = mid
                }
                
            } else if nums[mid] < target {
                start = mid + 1
            } else if nums[mid] > target {
                end = mid - 1
            }
        }
        
        if nums[start] != target {
            return -1
        }
        
        return start
    }
}
