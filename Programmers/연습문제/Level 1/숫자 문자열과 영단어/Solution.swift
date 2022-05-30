import Foundation

func solution(_ s:String) -> Int {
    let arr = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    var result = s
    for a in arr.enumerated() {
        result = result.replacingOccurrences(of: a.element, with: String(a.offset))
    }
    return Int(result) ?? 0
}


// TC
let s = "one4seveneight"
print(solution(s)) // 1478
