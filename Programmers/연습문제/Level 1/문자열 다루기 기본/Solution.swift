import Foundation

func solution(_ s:String) -> Bool {
    return s.range(of: "^(\\d{4}||\\d{6})$", options: .regularExpression) != nil
}
