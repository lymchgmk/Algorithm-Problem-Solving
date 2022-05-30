import Foundation

func solution(_ answers: [Int]) -> [Int] {
    let patterns = setPatterns()
    let scores = calcScores(answers, patterns)
    return getAnswer(scores)
}

func setPatterns() -> [[Int]] {
    let pattern1 = [1, 2, 3, 4, 5]
    let pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    let pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    return [pattern1, pattern2, pattern3]
}

func calcScores(_ answers: [Int], _ patterns: [[Int]]) -> [Int] {
    var scores = Array(repeating: 0, count: patterns.count)
    for (idx, pattern) in patterns.enumerated() {
        for j in 0..<answers.count {
            if answers[j] == pattern[j % pattern.count]
            {
                scores[idx] += 1
            }
        }
    }
    return scores
}

func getAnswer(_ scores: [Int]) -> [Int] {
    let maxScore = scores.max()
    return scores
        .enumerated()
        .filter{ $0.element == maxScore && $0.element > 0 }
        .sorted(by: { ($0.element, -$0.offset) > ($1.element, -$1.offset) })
        .map{ $0.offset + 1}
}


// TC
let answers = [1, 2, 3, 4, 5]
print(solution(answers)) // [1]
