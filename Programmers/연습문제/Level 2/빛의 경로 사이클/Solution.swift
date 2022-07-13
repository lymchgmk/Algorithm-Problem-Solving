import Foundation

func solution(_ grid:[String]) -> [Int] {
    let grid = grid.map{ Array($0) }
    let dirs: [(Int, Int)] = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    let (r_count, c_count, dirs_count) = (grid.count, grid[0].count, dirs.count)
    var visited = Array(repeating: Array(repeating: Array(repeating: false, count: dirs_count), count: c_count), count: r_count)
    
    func dfs(_ r: Int, _ c: Int, _ idx: Int, _ visited: inout [[[Bool]]]) -> Int {
        var (nr, nc, nidx) = (r, c, idx)
        var cycle_length = 0
        
        while !visited[nr][nc][nidx] {
            visited[nr][nc][nidx] = true
            cycle_length += 1
            
            nr = (nr + dirs[nidx].0 + r_count) % r_count
            nc = (nc + dirs[nidx].1 + c_count) % c_count
            if grid[nr][nc] == "R" {
                nidx = (nidx + 1 + dirs_count) % dirs_count
            } else if grid[nr][nc] == "L" {
                nidx = (nidx - 1 + dirs_count) % dirs_count
            }
        }
        return cycle_length
    }
    
    var answer: [Int] = []
    for r in 0..<grid.count {
        for c in 0..<grid[0].count {
            for idx in 0..<dirs.count {
                if !visited[r][c][idx] {
                    var cycle_length: Int = dfs(r, c, idx, &visited)
                    if cycle_length != 0 {
                        answer.append(cycle_length)
                    }
                }
            }
        }
    }
    return answer.sorted()
}


// TC
let grid = ["SL", "LR"]
print(solution(grid)) // [16]
