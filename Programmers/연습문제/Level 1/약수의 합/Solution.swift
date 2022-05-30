func solution(_ n:Int) -> Int {
    guard n != 0 else { return 0 }
    return Array(1...n).filter{ n % $0 == 0 }.reduce(0, +)
}

// TC
let n = 0
print(solution(n)) // 28
