import Foundation

func solution(_ numbers:String) -> Int {
    let arr = Array(numbers)
    var answer = 0
    var perms: Set<Int> = []
    for size in 1...arr.count {
        permutations(arr, size).forEach{
            perms.insert($0)
        }
    }
    return perms.filter{ isPrime($0) }.count
}

func permutations(_ arr: [Character], _ size: Int) -> [Int] {
    var result: [Int] = []
    var visited: [Bool] = Array(repeating: false, count: arr.count)
    
    func _permute(_ curr: [Character]) {
        print(arr, curr)
        if curr.count == size {
            let target = Int(curr.reduce(""){ $0 + String($1) })!
            result.append(target)
            return
        }
        
        for i in 0..<arr.count {
            if visited[i] == true { continue }
            visited[i] = true
            _permute(curr + [arr[i]])
            visited[i] = false
        }
    }

    _permute([])
    return result
}

func isPrime(_ n: Int) -> Bool {
    if n == 2 { return true }
    
    let root = Int(ceil(sqrt(Double(n))))
    if root < 2 { return false }
    for div in 2...root {
        if n % div == 0 {
            return false
        }
    }
    return true
}


// TC
let numbers = "1234"
print(solution(numbers)) // 3
