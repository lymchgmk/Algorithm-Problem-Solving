import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var craneMachine = CraneMachine(board)
    for move in moves {
        let col = move - 1
        craneMachine.pickUp(col)
    }
    return craneMachine.point
}

class CraneMachine {
    var point = 0
    var board: [[Int]]
    var stack: [Int] = []
    
    func pickUp(_ col: Int) -> Void {
        for row in 0..<board.count {
            if board[row][col] != 0 {
                stack.append(board[row][col])
                self.calcPoint()
                board[row][col] = 0
                return
            }
        }
    }
    
    func calcPoint() -> Void {
        if self.stack.count >= 2 {
            let last1 = self.stack.popLast() ?? 0
            let last2 = self.stack.popLast() ?? 0
            if last1 != 0 && last2 != 0 && last1 == last2 {
                self.point += 2
            } else {
                self.stack.append(last2)
                self.stack.append(last1)
            }
        }
    }
    
    init(_ board: [[Int]]) {
        self.board = board
    }
}


// TC
let board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
let moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves)) // 4
