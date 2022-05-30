import Foundation

func solution(_ n:Int) -> Int {
    return Int(String(String(n, radix: 3).reversed()), radix:3)!
}

    
// TC
let n = 45
print(solution(n)) // 7
