import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var reportCount: [String: Int] = [:]
    var reportWho: [String: [String]] = [:]
    
    for _report in Set(report) {
        let splitted = _report.split(separator: " ").map { String($0) }
        let (from, to) = (splitted[0], splitted[1])
        reportWho[from] = (reportWho[from] ?? []) + [to]
        reportCount[to] = (reportCount[to] ?? 0) + 1
    }
    
    return id_list.map { (id: String) -> Int in
        return (reportWho[id] ?? []).reduce(0) {
            $0 + ((reportCount[$1] ?? 0) >= k ? 1 : 0)
        }
    }
}


// TC
let id_list = ["muzi", "frodo", "apeach", "neo"]
let report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
let k = 2
print(solution(id_list, report, k)) // [2, 1, 1, 0]
