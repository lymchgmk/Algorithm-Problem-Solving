import Foundation

func solution(_ s:String) -> Int {
    if s.count == 1 { return 1 }
    
    var answer = s.count
    for length in (1...s.count/2) {
        let zipped_s = zipped(s, length)
        answer = min(answer, zipped_s.count)
    }
    return answer
}

func zipped(_ s: String, _ length: Int) -> String {
    var zippedResult = ""
    var zipWord = ""
    var zipCount = 1
    for i in stride(from: 0, to: s.count, by: length) {
        let startIndex = String.Index(utf16Offset: i, in: s)
        let endIndex = String.Index(utf16Offset: min(i+length, s.count), in: s)
        let word = String(s[startIndex..<endIndex])
        if word == zipWord {
            zipCount += 1
        } else {
            zippedResult += (zipCount > 1 ? String(zipCount) : "") + zipWord
            zipWord = word
            zipCount = 1
        }
    }
    zippedResult += (zipCount > 1 ? String(zipCount) : "") + zipWord
    return zippedResult
}


// TC
let s = "aabbaccc"
print(solution(s)) // 7
