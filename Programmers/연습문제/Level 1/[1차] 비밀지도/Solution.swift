func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    return (0..<n).map {
        let row = String(arr1[$0] | arr2[$0], radix: 2)
        let padding = String(repeating: "0", count: n - row.count )
        let paddedRow = padding + row
        return paddedRow.reduce("") { $0 + ($1 == "1" ? "#" : " ") }
    }
}

    
// TC
let n = 5
let arr1 = [9, 20, 28, 18, 11]
let arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
