func solution(_ n:Int) -> String {
    return String(repeating: "수박", count: n/2) + (n % 2 == 0 ? "" : "수")
}


// TC
let n = 3
print(solution(n))
