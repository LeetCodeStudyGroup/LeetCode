class Solution {
    func subsets(_ nums: [Int]) -> [[Int]] {
        let sorted = nums.sorted()
        return [[]] + subTree(tempRoot: [], nums: sorted, startIndex: 0)
    }
    
    func subTree(tempRoot: [Int], nums: [Int], startIndex: Int) -> [[Int]] {
        
        var result = [[Int]]()
        
        for index in startIndex ..< nums.count {
            let subTempRoot = tempRoot + [nums[index]]
            result = result + [subTempRoot] + subTree(tempRoot: subTempRoot, nums: nums, startIndex: index+1)
        }
        
        return result
    }
}
