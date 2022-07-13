import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    let days = calcDays(progresses, speeds)
    var answer: [Int] = []
    var maxDay = days.first ?? 0
    var count = 0
    while !days.isEmpty {
        let day = days.pop() ?? 0
        if day <= maxDay {
            count += 1
        } else {
            answer.append(count)
            maxDay = day
            count = 1
        }
    }
    answer.append(count)
    return answer
}

func calcDays(_ progresses: [Int], _ speeds: [Int]) -> Queue<Int> {
    let days = zip(progresses, speeds).map {
        Int(ceil(Double(100 - $0) / Double($1)))
    }
    return Queue(days)
}

class Queue<T: Equatable> {
    var enqueue: [T]
    var dequeue: [T] = []
    
    var isEmpty: Bool {
        return enqueue.isEmpty && dequeue.isEmpty
    }
    
    var first: T? {
         if dequeue.isEmpty {
             return enqueue.first
         } else {
             return dequeue.last
         }
     }
    
    var last: T? {
        if enqueue.isEmpty {
            return dequeue.first
        } else {
            return enqueue.last
        }
    }

    init(_ queue: [T]) {
        enqueue = queue
    }
    
    func push(_ n: T) {
        enqueue.append(n)
    }
    
    func pop() -> T? {
        if dequeue.isEmpty {
            dequeue = enqueue.reversed()
            enqueue.removeAll()
        }
        return dequeue.popLast()
    }
    
    func removeAll() {
        enqueue.removeAll()
        dequeue.removeAll()
    }
}


// TC
let progresses = [95, 90, 99, 99, 80, 99]
let speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds)) // [1, 3, 2]
