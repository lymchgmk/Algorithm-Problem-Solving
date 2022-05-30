func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    let answer = getSum(arr1: arr1, arr2:arr2)
    return answer
}

func getSum(arr1: [[Int]], arr2: [[Int]]) -> [[Int]] {
    let (r, c) = (arr1.count, arr1[0].count)
    var _answer = setDefualtArr(r: r, c: c)
    for _r in 0..<r {
        for _c in 0..<c {
            _answer[_r][_c] = arr1[_r][_c] + arr2[_r][_c]
        }
    }
    return _answer
}

func setDefualtArr(r: Int, c: Int) -> [[Int]] {
    return Array(repeating: Array(repeating:0, count: c), count: r)
}


// TC
let arr1 = [[1],[2]]
let arr2 = [[3],[4]]
print(solution(arr1, arr2))
