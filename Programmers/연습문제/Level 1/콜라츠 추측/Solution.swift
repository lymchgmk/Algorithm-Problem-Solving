func solution(_ num:Int) -> Int {
    return isCollatz(num)
}

func isCollatz(_ num: Int) -> Int {
    var count = 0
    let maxCount = 500
    var _num = num
    
    while count < maxCount && _num != 1{
        _num = doCollatz(_num)
        count += 1
    }
    
    return count < maxCount ? count : -1
}

func doCollatz(_ num: Int) -> Int{
    if num.isMultiple(of: 2) {
        return num / 2
    } else {
        return num * 3 + 1
    }
}


// TC
let num = 6
print(solution(num))
