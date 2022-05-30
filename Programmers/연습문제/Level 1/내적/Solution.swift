import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    return zip(a, b).map(*).reduce(0, +)
}


// TC
let a = [1, 2, 3, 4]
let b = [-3, -1, 0, 2]
print(solution(a, b)) // 3
