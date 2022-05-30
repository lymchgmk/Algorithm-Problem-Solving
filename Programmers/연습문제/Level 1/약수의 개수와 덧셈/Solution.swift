import Foundation


func solution(_ left:Int, _ right:Int) -> Int {
    var answer = 0
    (left...right).map {
        if isSquared($0) {
            answer -= $0
        } else {
            answer += $0
        }
    }
    return answer
}

func isSquared(_ num: Int) -> Bool {
    let root = Int(sqrt(Double(num)))
    return root * root == num
}

    
// TC
let left = 24
let right = 27
print(solution(left, right)) // 43
