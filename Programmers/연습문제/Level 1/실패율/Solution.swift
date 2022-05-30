import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    let stucked = calcStucked(N, stages)
    let failures = calcFailures(N, stages, stucked)
    let answer = getAnswer(failures)
    return answer
}

func calcStucked(_ N: Int, _ stages: [Int]) -> [Int] {
    var stucked = Array(repeating: 0, count: N+1)
    for stage in stages {
        stucked[stage-1] += 1
    }
    return stucked
}

func calcFailures(_ N: Int, _ stages: [Int], _ stucked: [Int]) -> [Float] {
    var failures = Array(repeating: Float(0), count: N)
    var players = stages.count
    for i in 0..<N {
        failures[i] = Float(stucked[i]) / Float(players)
        players -= stucked[i]
    }
    return failures
}

func getAnswer(_ failures: [Float]) -> [Int] {
    return failures
        .enumerated()
        .sorted(by: { ($0.element, -$0.offset) > ($1.element, -$1.offset) })
        .map{ $0.offset + 1}
}

    
// TC
let N = 5
let stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages)) // [3, 4, 2, 1, 5]
