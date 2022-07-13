import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var counter: [String: [String]] = [:]
    for cloth in clothes {
        counter[cloth[1]] = (counter[cloth[1]] ?? []) + [cloth[0]]
    }
    
    var answer = 1
    counter.forEach{
        answer *= ($0.value.count + 1)
    }
    return answer - 1
}


// TC
let clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes)) // 5
