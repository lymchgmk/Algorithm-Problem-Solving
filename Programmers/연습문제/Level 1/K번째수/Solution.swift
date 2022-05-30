import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    return commands.map {
        let (i, j, k) = ($0[0]-1, $0[1]-1, $0[2]-1)
        return array[i...j].sorted()[k]
    }
}

// TC
let array = [1, 5, 2, 6, 3, 7, 4]
let commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands)) // [5, 6, 3]
