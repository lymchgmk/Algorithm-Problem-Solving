import Foundation


func solution(_ a:Int, _ b:Int) -> String {
    let calendar = Calendar(identifier: .gregorian)
    let dateComponents = DateComponents(year: 2016, month: a, day: b)
    let date = calendar.date(from: dateComponents)
    let dateFormatter = DateFormatter()
    dateFormatter.locale = Locale(identifier: "en_US")
    dateFormatter.dateFormat = "EE"
    return dateFormatter.string(from: date!).uppercased()
}

    
// TC
let a = 5
let b = 24
print(solution(a, b))
