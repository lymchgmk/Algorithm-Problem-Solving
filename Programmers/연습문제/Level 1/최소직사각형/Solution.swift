import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var (max_w, max_h) = (0, 0)
    for size in sizes {
        max_w = max(max_w, size.max()!)
        max_h = max(max_h, size.min()!)
    }
    return max_w * max_h
}

    
// TC
let sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
