import Foundation

func solution(_ phone_number:String) -> String {
    let pattern = "\\d(?=\\d{4})"
    let regex = try! NSRegularExpression(pattern: pattern, options: [])
    let answer = regex.stringByReplacingMatches(in: phone_number, options: [], range: NSRange(0..<phone_number.count), withTemplate: "*")
    return answer
}


// TC
let phone_number = "01033334444"
print(solution(phone_number)) // "*******4444"
