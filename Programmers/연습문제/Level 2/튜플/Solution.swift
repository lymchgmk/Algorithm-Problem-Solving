import Foundation

func solution(_ s:String) -> [Int] {
    let numbers = s.components(separatedBy: ["{", "}", ","]).filter{ $0 != "" }.map{ Int($0)! }
    let counter = countNumbers(numbers)
    return getTuple(counter)
}

func countNumbers(_ numbers: [Int]) -> [Int: Int] {
    var counter: [Int: Int] = [:]
    for number in numbers {
        counter[number] = (counter[number] ?? 0) + 1
    }
    return counter
}

func getTuple(_ counter: [Int: Int]) -> [Int] {
    return counter.sorted(by: { $0.value > $1.value }).map{ $0.key }
}


// TC
let s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s)) // [2, 1, 3, 4]
