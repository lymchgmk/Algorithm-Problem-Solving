import Foundation

func solution(_ numbers:[Int], _ target:Int) -> Int {
    
    func dfs(_ idx: Int, _ sum: Int) -> Void {
        if idx == numbers.count {
            if sum == target { answer += 1 }
            return
        }
        dfs(idx+1, sum + numbers[idx])
        dfs(idx+1, sum - numbers[idx])
    }
    
    var answer = 0
    dfs(0, 0)
    return answer
}


// TC
let numbers = [1, 1, 1, 1, 1]
let target = 3
print(solution(numbers, target)) // 5
