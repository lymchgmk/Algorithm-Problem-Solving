import Foundation

func solution(_ rows:Int, _ columns:Int, _ queries:[[Int]]) -> [Int] {
    var board = Board(rows, columns)
    for query in queries {
        board.rotate(query)
    }
    return board.minNums
}

struct Board {
    var data: [[Int]]
    var minNums: [Int]
    
    init(_ rows: Int, _ columns: Int) {
        data = Array(repeating: Array(repeating: 0, count: columns), count: rows)
        var number = 1
        for r in (0..<rows) {
            for c in (0..<columns) {
                data[r][c] = number
                number += 1
            }
        }
        
        minNums = []
    }
    
    mutating func rotate(_ query: [Int]) -> Void {
        let (r1, c1, r2, c2) = (query[0]-1, query[1]-1, query[2]-1, query[3]-1)
        var minNum = self.data.count * self.data[0].count
        var before = 0, after = 0
        
        for c in c1..<c2 {
            minNum = min(minNum, self.data[r1][c])
            after = self.data[r1][c]
            self.data[r1][c] = before
            before = after
        }
        
        for r in r1..<r2 {
            minNum = min(minNum, self.data[r][c2])
            after = self.data[r][c2]
            self.data[r][c2] = before
            before = after
        }
        
        for c in (c1+1...c2).reversed() {
            minNum = min(minNum, self.data[r2][c])
            after = self.data[r2][c]
            self.data[r2][c] = before
            before = after
        }

        for r in (r1+1...r2).reversed() {
            minNum = min(minNum, self.data[r][c1])
            after = self.data[r][c1]
            self.data[r][c1] = before
            before = after
        }
        
        self.data[r1][c1] = after
        
        self.minNums.append(minNum)
    }
}


// TC
let rows = 3
let columns = 3
let querys = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
print(solution(rows, columns, querys)) // [8, 10, 25]
