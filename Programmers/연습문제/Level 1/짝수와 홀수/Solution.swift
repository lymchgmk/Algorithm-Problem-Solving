func solution(_ num:Int) -> String {
    return num % 2 == 0 ? "Even" : "Odd"
}


// TC
let num = 3
print(solution(num)) // "Odd"
