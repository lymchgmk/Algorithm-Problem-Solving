func solution(_ s:String) -> String {
    let startIndex = String.Index(utf16Offset: (s.count-1)/2, in: s)
    let endIndex = String.Index(utf16Offset: s.count/2, in: s)
    return String(s[startIndex...endIndex])
}

    
// TC
let s = "abcdf"
print(solution(s))
