import Foundation

func solution(_ s:String) -> String {
    let words = splitString(s)
    var answer: [String] = []
    for word in words {
        answer.append(makeWeird(word))
    }
    return answer.joined(separator: " ")
}

func splitString(_ s: String) -> [String] {
    return s.components(separatedBy: " ")
}

func makeWeird(_ word: String) -> String {
    var weirdWord = ""
    for (idx, char) in word.enumerated() {
        if idx % 2 == 0 {
            weirdWord += char.uppercased()
        } else {
            weirdWord += char.lowercased()
        }
    }
    return weirdWord
}


let s: String = "try hello world"
print(solution(s))
