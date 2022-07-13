import Foundation

func solution(_ p:String) -> String {
    // #1
    if p.isEmpty { return "" }
    
    // #2
    var index = p.startIndex
    repeat {
        index = p.index(after: index)
    } while !isBalanced(String(p[..<index]))
    var u = String(p[..<index]), v = String(p[index...])
    
    // #3
    if isCollect(u) {
        // #3-1
        return u + solution(v)
    // #4
    } else {
        u.removeLast()
        u.removeFirst()
        return "(" + solution(v) + ")" + u.map{ String($0) == "(" ? ")" : "(" }.joined()
    }
}

func isBalanced(_ str: String) -> Bool {
    return str.filter{ $0 == "(" }.count == str.filter{ $0 == ")" }.count
}

func isCollect(_ str: String) -> Bool {
    var stack: [String] = []
    str.forEach {
        if stack.isEmpty {
            stack.append(String($0))
        } else {
            if stack.last! == "(" && String($0) == ")" {
                stack.removeLast()
            } else {
                stack.append(String($0))
            }
        }
    }
    return stack.isEmpty
}


// TC
let p = "(()())()"
print(solution(p)) // "(()())()"
