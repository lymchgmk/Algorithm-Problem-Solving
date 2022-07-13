import Foundation

func solution(_ s:String) -> Int{
    let removed = removePairs(s)
    return removed.isEmpty ? 1 : 0
}

func removePairs(_ s: String) -> String {
    var stack: [String] = []
    for char in s {
        let char = String(char)
        if stack.isEmpty {
            stack.append(char)
        }
        else {
            if stack.last! == char {
                stack.popLast()
            } else {
                stack.append(char)
            }
        }
    }
    return stack.joined()
}


// TC
let s = "baabaa"
print(solution(s)) // 1
