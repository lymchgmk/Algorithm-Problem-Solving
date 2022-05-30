import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    let gymsuits = setGymsuits(n, lost, reserve)
    let answer = borrowReserve(n, gymsuits)
    return answer
}

func setGymsuits(_ n: Int, _ lost: [Int], _ reserve: [Int]) -> [Int] {
    var gymsuits = Array(repeating: 1, count: n)
    for i in lost {
        gymsuits[i-1] -= 1
    }
    for j in reserve {
        gymsuits[j-1] += 1
    }
    return gymsuits
}

func borrowReserve(_ n: Int, _ gymsuits: [Int]) -> Int {
    var gymsuits = gymsuits
    for i in 0..<n {
        if gymsuits[i] >= 2 {
            if i != 0 && gymsuits[i-1] == 0 {
                gymsuits[i] -= 1
                gymsuits[i-1] += 1
            } else if i != n-1 && gymsuits[i+1] == 0 {
                gymsuits[i] -= 1
                gymsuits[i+1] += 1
            }
        }
    }
    return gymsuits.filter{ $0 >= 1 }.count
}

    
// TC
let n = 5
let lost = [2, 4]
let reserve = [1, 3, 5]
print(solution(n, lost, reserve)) // 5
