import Foundation

func solution(_ expression:String) -> Int64 {
    let numbers = expression.components(separatedBy: ["+", "-", "*"]).map{ Int($0)! }
    let operators = Array(expression.filter{ !$0.isNumber }).map{ String($0) }
    let priorities = permutation(["+", "-", "*"], 2)
    var maxValue: Int64 = 0
    for priority in priorities {
        let currValue: Int64 = calcValue(numbers, operators, priority)
        maxValue = max(maxValue, abs(Int64(currValue)))
    }
    return maxValue
}

func permutation<T>(_ arr: [T], _ n: Int) -> [[T]] {
    if n == 0 { return [arr] }
    
    var arr = arr
    var ret = permutation(arr, n-1)
    for i in 0..<n {
        arr.swapAt(i, n)
        ret += permutation(arr, n-1)
        arr.swapAt(i, n)
    }
    return ret
}

func calcValue(_ numbers: [Int], _ operators: [String], _ priority: [String]) -> Int64 {
    var (numbers, operators) = (numbers, operators)
    for prior_operator in priority {
        while let idx = operators.firstIndex(of: prior_operator) {
            switch prior_operator {
            case "+": numbers[idx] = numbers[idx] + numbers[idx+1]
            case "-": numbers[idx] = numbers[idx] - numbers[idx+1]
            case "*": numbers[idx] = numbers[idx] * numbers[idx+1]
            default:
                break
            }
            numbers.remove(at: idx+1)
            operators.remove(at: idx)
        }
    }
    return Int64(numbers[0])
}


// TC
let expression = "100-200*300-500+20"
print(solution(expression)) // 60420
