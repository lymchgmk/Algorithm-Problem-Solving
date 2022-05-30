import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var result: [Int] = []
    for i in 0..<numbers.count {
        for j in i+1..<numbers.count {
            result.append(numbers[i] + numbers[j])
        }
    }
    return Array(Set(result)).sorted()
}
