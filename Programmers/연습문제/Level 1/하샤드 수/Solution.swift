func solution(_ x:Int) -> Bool {
    return isHashad(x)
}

func isHashad(_ x: Int) -> Bool{
    let sum = getDigitSum(x)
    return (x % sum) == 0
}

func getDigitSum(_ x: Int) -> Int{
    return String(x)
        .map{ Int(String($0))! }
        .reduce(0, +)
}

// TC
let arr = 13
print(solution(arr))
