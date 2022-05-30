import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    return zip(absolutes, signs).map { $0 * ($1 == true ? 1 : -1) }.reduce(0, +)
}

// TC
let absolutes = [4, 7, 12]
let signs = [true, false, true]
print(solution(absolutes, signs)) // 9
