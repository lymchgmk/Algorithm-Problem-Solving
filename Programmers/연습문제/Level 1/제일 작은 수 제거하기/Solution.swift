func solution(_ arr:[Int]) -> [Int] {
    let minValue = arr.min()
    var answer: [Int] = []
    for value in arr {
        if value != minValue {
            answer.append(value)
        }
    }
    return answer.isEmpty ? [-1] : answer
}


// TC
let arr = [4, 3, 2, 1]
print(solution(arr)) // "Odd"
