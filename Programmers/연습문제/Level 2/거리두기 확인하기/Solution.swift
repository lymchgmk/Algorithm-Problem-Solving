import Foundation

func solution(_ places:[[String]]) -> [Int] {
    let places = places.map { $0.map { Array($0) } }
    return places.map {
        keepDistance($0) ? 1 : 0
    }
}

func keepDistance(_ place: [[Character]]) -> Bool {
    func dfs(_ r: Int, _ c: Int) -> Bool {
        var stack: [[Int]] = [[r, c, 0]]
        stack.append([r, c, 0])
        var visited = Set<[Int]>()
        visited.insert([r, c])
        let dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while !stack.isEmpty {
            let curr = stack.popLast()!
            for dir in dirs {
                let (post_r, post_c, post_cnt) = (curr[0]+dir[0], curr[1]+dir[1], curr[2]+1)
                if (0<=post_r && post_r<5 && 0<=post_c && post_c<5) && post_cnt<=2 && !visited.contains([post_r, post_c]) {
                    visited.insert([post_r, post_c])
                    if place[post_r][post_c] == "P" {
                        return false
                    } else if place[post_r][post_c] == "O" {
                        stack.append([post_r, post_c, post_cnt])
                    }
                }
            }
        }
        return true
    }

    for r in 0..<5 {
        for c in 0..<5 {
            if place[r][c] == "P"{
                if !dfs(r, c) {
                    return false
                }
            }
        }
    }
    return true
}


// TC
let places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places)) // [1, 0, 1, 1, 1]
