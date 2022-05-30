import Foundation

func solution(_ n:Int) -> Int {
    for div in (2...n) {
        if n % div == 1 {
            return div
        }
    }
    return 0
}
