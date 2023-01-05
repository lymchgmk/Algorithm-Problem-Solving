import Foundation

var myBoard: [[Int]] = []
var rows = 0
var cols = 0
let dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
var visited: [[Bool]] = []

struct Location {
    let row: Int
    let col: Int

    init(row: Int, col: Int) {
        self.row = row
        self.col = col
    }
}

func solution(_ board:[[Int]], _ aloc:[Int], _ bloc:[Int]) -> Int {
    myBoard = board
    rows = myBoard.count
    cols = myBoard[0].count
    visited = Array(repeating: Array(repeating: false, count: cols), count: rows)

    let startPlayerLocation = Location(row: aloc[0], col: aloc[1])
    let startEnemyLocation = Location(row: bloc[0], col: bloc[1])

    return solve(playerLocation: startPlayerLocation, enemyLocation: startEnemyLocation)
}

func solve(playerLocation: Location, enemyLocation: Location) -> Int {
    let (currR, currC) = (playerLocation.row, playerLocation.col)

    if visited[playerLocation.row][playerLocation.col] { return 0 }

    var turns = 0
    for (dirR, dirC) in dirs {
        let postPlayerLocation = Location(row: playerLocation.row + dirR,
                                          col: playerLocation.col + dirC)
        let (postR, postC) = (postPlayerLocation.row, postPlayerLocation.col)

        if isOutOfBounds(location: postPlayerLocation) || visited[postR][postC] || myBoard[postR][postC] == 0 {
            continue
        }

        visited[currR][currC] = true
        let val = solve(playerLocation: enemyLocation, enemyLocation: postPlayerLocation) + 1
        visited[currR][currC] = false

        if turns % 2 == 0 && val % 2 == 1 {
            turns = val
        } else if turns % 2 == 0 && val % 2 == 0 {
            turns = max(turns, val)
        } else if turns % 2 == 1 && val % 2 == 1 {
            turns = min(turns, val)
        }
    }

    return turns
}

func isOutOfBounds(location: Location) -> Bool {
    return location.row < 0 || rows <= location.row || location.col < 0 || cols <= location.col
}

let board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
let aloc = [1, 0]
let bloc = [1, 2]
print(solution(board, aloc, bloc)) // 5
