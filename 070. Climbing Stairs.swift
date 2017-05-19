class Solution {
    func climbStairs(_ n: Int) -> Int {
        var map = Dictionary<Int, Int>()

        map[0] = 1
        map[1] = 2
        
        if n < 2 {
            return map[n-1]!
        }
        
        for i in 2 ..< n {
            map[i] = map[i - 1]! + map[i - 2]!
        }
        
        return map[n-1]!
    }
}
