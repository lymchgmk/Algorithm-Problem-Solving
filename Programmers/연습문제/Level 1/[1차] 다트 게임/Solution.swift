import Foundation


func solution(_ dartResult:String) -> Int {
    let darts = splitDarts(dartResult)
    let points = calcPoints(darts)
    let answer = calcSum(points)
    return answer
}

func splitDarts(_ dartResult: String) -> [[String:String]] {
    
    func _getMatches(_ dartResult: String) -> [NSTextCheckingResult] {
        let pattern = "(?<score>\\d{1,2})(?<bonus>[SDT])(?<option>[*#]?)"
        let regex = try! NSRegularExpression(pattern: pattern, options: [])
        let range = NSRange(dartResult.startIndex..., in: dartResult)
        let _matches = regex.matches(in: dartResult, options:[], range: range)
        return _matches
    }

    func _matches2darts(_ matches: [NSTextCheckingResult]) -> [[String:String]] {
        var darts: [[String: String]] = []
        let names = ["score", "bonus", "option"]
        for match in matches {
            var dart: [String: String] = [:]
            for name in names {
                let matchRange = match.range(withName: name)
                if let substringRange = Range(matchRange, in: dartResult) {
                    dart[name] = String(dartResult[substringRange])
                }
            }
            darts.append(dart)
        }
        return darts
    }
    
    let matches = _getMatches(dartResult)
    let darts = _matches2darts(matches)
    return darts
}

func calcPoints(_ darts: [[String: String]]) -> [Int] {
    let calcDict = ["S": 1, "D": 2, "T": 3, "#": -1, "*": 2]
    
    func _getPoint(_ dart: [String: String]) -> Int {
        let (score, bonus) = (Int(dart["score"]!)!, calcDict[dart["bonus"]!]!)
        return _pow(score, bonus)
    }
    
    func _pow(_ score: Int, _ bonus: Int) -> Int {
        var result = 1
        for _ in 1...bonus {
            result *= score
        }
        return result
    }
    
    var points = Array(repeating: 0, count: darts.count)
    for (idx, dart) in darts.enumerated() {
        points[idx] += _getPoint(dart)
        if let option = calcDict[dart["option"]!] {
            points[idx] *= option
            if option == 2 && idx >= 1 {
                points[idx-1] *= option
            }
        }
    }
    return points
}

func calcSum(_ points: [Int]) -> Int {
    return points.reduce(0, +)
}
    
// TC
let dartResult = "1S*2T*3S"
print(solution(dartResult))
