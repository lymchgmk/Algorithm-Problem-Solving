import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int {
    var a: Int = a
    var b: Int = b
    var answer: Int = 0
    while a != b {
        a = Int((a+1)/2)
        b = Int((b+1)/2)
        answer += 1
    }

    return answer
}
