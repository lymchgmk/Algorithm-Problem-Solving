import Foundation


func solution(_ n:Int) -> Int {
    return (2...n).filter{ isPrime($0) }.count
}

func isPrime(_ n: Int) -> Bool {
    if n == 2 { return true }
    
    let root = Int(ceil(sqrt(Double(n))))
    for div in 2...root {
        if n % div == 0 {
            return false
        }
    }
    return true
}


// TC
let n = 10
print(solution(n))
