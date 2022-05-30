import Foundation

func solution(_ nums:[Int]) -> Int {
    var answer = 0
    for i in 0..<nums.count {
        for j in i+1..<nums.count {
            for k in j+1..<nums.count {
                let sum = nums[i] + nums[j] + nums[k]
                if isPrime(sum) {
                    answer += 1
                }
            }
        }
    }
    return answer
}

func isPrime(_ num: Int) -> Bool {
    for div in 2...Int(sqrt(Double(num))) {
        if num % div == 0 {
            return false
        }
    }
    return true
}


// TC
let nums = [1, 2, 3, 4]
print(solution(nums)) // 1
