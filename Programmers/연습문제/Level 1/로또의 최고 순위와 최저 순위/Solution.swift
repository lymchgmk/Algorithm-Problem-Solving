import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    let rankingDict = [6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6]
    let minWin: Int = lottos.filter { win_nums.contains($0) }.count
    let countZero: Int = lottos.filter { $0 == 0 }.count
    return [rankingDict[minWin + countZero]!, rankingDict[minWin]!]
}


// TC
let lottos = [44, 1, 0, 0, 31, 25]
let win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums)) // [3, 5]
