func solution(_ strings:[String], _ n:Int) -> [String] {
    return strings.sorted{
        Array($0)[n] != Array($1)[n] ? Array($0)[n] < Array($1)[n] : $0 < $1
    }
}


// TC
let strings = ["abce", "abcd", "cdx"]
let n = 2
print(solution(strings, n))
