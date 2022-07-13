func solution(_ str1:String, _ str2:String) -> Int {
    let elements1 = makeElements(str1), elements2 = makeElements(str2)
    let sizeInter = sizeIntersection(elements1, elements2)
    let sizeUnion = sizeUnionsection(elements1, elements2)
    let jacard = getJacard(sizeInter, sizeUnion)
    return jacard
}

func makeElements(_ str: String) -> [String: Int] {
    var elements: [String: Int] = [:]
    let str = str.lowercased()
    for offset in 0..<str.count-1 {
        let startIndex = String.Index(utf16Offset: offset, in: str)
        let endIndex = String.Index(utf16Offset: offset+2, in: str)
        let subStr = String(str[startIndex..<endIndex])
        if ("a"..."z").contains(subStr.first!) && ("a"..."z").contains(subStr.last!) {
            elements[subStr] = (elements[subStr] ?? 0) + 1
        }
    }
    return elements
}

func sizeIntersection(_ elements1: [String: Int], _ elements2: [String: Int]) -> Int {
    var size = 0
    for key in elements1.keys {
        if elements2.keys.contains(key) {
            size += min(elements1[key]!, elements2[key]!)
        }
    }
    return size
}

func sizeUnionsection(_ elements1: [String: Int], _ elements2: [String: Int]) -> Int {
    var size = 0
    for key in Set(Array(elements1.keys) + Array(elements2.keys)) {
        size += max(elements1[key] ?? 0, elements2[key] ?? 0)
    }
    return size
}

func getJacard(_ sizeInter: Int, _ sizeUnion: Int) -> Int {
    if sizeInter == 0 && sizeUnion == 0 {
        return 65536
    }
    return Int((Double(sizeInter) / Double(sizeUnion)) * 65536)
}


// TC
let str1 = "FRANCE"
let str2 = "french"
print(solution(str1, str2)) // "16384"
