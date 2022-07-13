import Foundation

func solution(_ name:String) -> Int {
    let name = name.utf8.map{ min(Int($0) - 65, 90 - Int($0) + 1) }

    let count_updown = name.reduce(0, +)
    
    var count_leftright = name.count - 1
    let start_idx = 0
    for right_limit_idx in 0..<name.count {
        var left_limit_idx = right_limit_idx + 1
        while left_limit_idx < name.count && name[left_limit_idx] == 0 {
            left_limit_idx += 1
        }
        let min_plus_distance = min(right_limit_idx - start_idx, name.count - left_limit_idx)
        count_leftright = min(count_leftright, (right_limit_idx - start_idx) + (name.count - left_limit_idx) + min_plus_distance)
    }
    
    return count_updown + count_leftright
}


// TC
let name = "JAAAN"
print(solution(name)) // 23
