class Solution {
    var islandCount = 0
    
    var tempGrid = [[Character]]()
    
    func numIslands(_ grid: [[Character]]) -> Int {
        
        if grid.count == 0 || grid[0].count == 0 {
            return 0
        }
        
        tempGrid = grid
        
        // loop all node
        for x in 0 ..< tempGrid.count {
            for y in 0 ..< tempGrid[0].count {
                if tempGrid[x][y] == "1" {
                    markByBfs(&tempGrid, x, y)
                    islandCount += 1
                }
            }
        }
        
        return islandCount
    }
    
    struct Coordinate {
        var x: Int
        var y: Int
    }
    
    // bfs to check islands
    func markByBfs(_ grid: inout [[Character]], _ x: Int, _ y: Int) {
        // magic numbers!
        let directionX = [0, 1, -1, 0]
        let directionY = [1, 0, 0, -1]
        
        var queue = Queue<Coordinate>()
        queue.enqueue(Coordinate(x: x, y: y))
        
        while !queue.isEmpty {
            if let pop = queue.dequeue() {
                for i in 0 ..< directionX.count {
                    let adjPointX = pop.x + directionX[i]
                    let adjPointY = pop.y + directionY[i]
                    if isOutBound(adjPointX, adjPointY) {
                        continue
                    }
                    
                    if grid[adjPointX][adjPointY] == "1" {
                        queue.enqueue(Coordinate(x: adjPointX, y: adjPointY))
                        grid[adjPointX][adjPointY] = "0"
                    }
                }
            }
        }
    }
    
    func isOutBound(_ x: Int, _ y: Int) -> Bool {
        if x < 0 || x >= tempGrid.count || y < 0 || y >= tempGrid[0].count {
            return true
        }
        
        return false
    }
}

public struct Queue<T> {
    fileprivate var array = [T]()
    
    public var isEmpty: Bool {
        return array.isEmpty
    }
    
    public var count: Int {
        return array.count
    }
    
    public mutating func enqueue(_ element: T) {
        array.append(element)
    }
    
    public mutating func dequeue() -> T? {
        if isEmpty {
            return nil
        } else {
            return array.removeFirst()
        }
    }
    
    public var front: T? {
        return array.first
    }
}
