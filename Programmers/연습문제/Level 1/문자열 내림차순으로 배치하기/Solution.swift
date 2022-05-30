func solution(_ s:String) -> String {
    return s.sorted { $0 > $1 }.reduce("") { String($0) + String($1) }
}


// TC
let s = "Zbcdefg"
print(solution(s))
