import Foundation

func solution(_ new_id:String) -> String {
    let id1 = step1(new_id)
    let id2 = step2(id1)
    let id3and4 = step3and4(id2)
    let id5 = step5(id3and4)
    let id6 = step6(id5)
    let id7 = step7(id6)
    return id7
}

func step1(_ id: String) -> String {
    return id.lowercased()
}

func step2(_ id: String) -> String {
    let alphaRange = ("a"..."z")
    let symbolArray = ["-", "_", "."]
    return id.filter {  alphaRange.contains(String($0)) || $0.isNumber || symbolArray.contains(String($0)) }
}

func step3and4(_ id: String) -> String {
    return id.split(separator: ".").joined(separator: ".")
}

func step5(_ id: String) -> String {
    return id.isEmpty ? "a" : id
}

func step6(_ id: String) -> String {
    if id.count <= 15 {
        return id
    }
    
    let startIndex = id.startIndex
    let endIndex = id.index(id.startIndex, offsetBy: 15)
    var new_id = String(id[startIndex..<endIndex])
    if new_id.last! == "." {
        new_id = String(new_id.dropLast())
    }
    return new_id
}

func step7(_ id: String) -> String {
    if id.count > 2 {
        return id
    }
    
    let lastChar = id.last!
    return id + String(repeating: lastChar, count: 3 - id.count)
}



// TC
let new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id)) // "bat.y.abcdefghi"
