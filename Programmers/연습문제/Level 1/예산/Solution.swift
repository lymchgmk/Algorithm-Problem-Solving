import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var total = 0
    var count = 0
    d.sorted().map {
        if total + $0 <= budget {
            total += $0
            count += 1
        }
    }
    return count
}

    
// TC
let d = [1, 3, 2, 5, 4]
let budget = 9
print(solution(d, budget)) // 3
