func solution(_ s:String, _ n:Int) -> String {
    return s.utf8.map {
        var code = Int($0)
        switch code {
        case 65...90:
            code = (code + n - 65) % 26 + 65
        case 97...122:
            code = (code + n - 97) % 26 + 97
        default:
            break
        }
        return String(UnicodeScalar(code)!)
    }.joined()
}


// TC
let s = "z"
let n = 1
print(solution(s, n)) // 28
