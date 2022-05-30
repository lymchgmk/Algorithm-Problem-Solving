func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    let sortedArr = arr.sorted()
    let answer = sortedArr.filter{ $0 % divisor == 0}
    return answer.isEmpty ? [-1] : answer
}
