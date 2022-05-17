import Foundation

func solution(_ x:Int, _ n:Int) -> [Int64] {
    var answer: [Int64] = []
    
    for i in stride(from: 0, to: n, by: 1) {
        answer.append(Int64(x + x*i))
    }
    return answer
}

