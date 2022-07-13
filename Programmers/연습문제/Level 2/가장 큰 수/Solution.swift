import Foundation

func solution(_ numbers:[Int]) -> String {
    let stringNumbers = numbers.map{ String($0) }
    let sortedStringNumbers = stringNumbers.sorted{ $0 + $1 > $1 + $0 }
    let maxNumberString = sortedStringNumbers.reduce(""){ $0 + $1 }
    return maxNumberString.first == "0" ? "0" : maxNumberString
}


// TC
let numbers = [3, 30, 34, 5, 9]
print(solution(numbers)) // "9534330"
