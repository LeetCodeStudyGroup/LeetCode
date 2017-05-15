class Solution {
    func sortColors(_ nums: inout [Int]) {
        
        if nums.count == 0 {
            return
        }
        
        var left = nums.startIndex
        var right = nums.endIndex - 1
        
        var i = 0
        while i <= right {
            if nums[i] == 0 {
                swap(&nums[left], &nums[i])
                left += 1
                i += 1
            } else if nums[i] == 2 {
                swap(&nums[right], &nums[i])
                right -= 1
            } else {
                i += 1
            }
        }
    }
    
    func swap(_ item1: inout Int, _ item2: inout Int) {
        let temp = item1
        item1 = item2
        item2 = temp
    }
}
