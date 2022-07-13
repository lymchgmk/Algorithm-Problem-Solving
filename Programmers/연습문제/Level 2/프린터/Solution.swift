import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var deque: Deque<(Int, Int)> = Deque(priorities.enumerated().map{ ($0.element, $0.offset) })
    var answer = 0
    while !deque.isEmpty {
        let curr_doc = deque.popFirst()!
        var flag = false
        for doc in deque.enQueue + deque.deQueue {
            if curr_doc.0 < doc.0 {
                deque.pushLast(curr_doc)
                flag = true
                break
            }
        }
        
        if !flag {
            answer += 1
            if curr_doc.1 == location {
                break
            }
        }
    }
    return answer
}

struct Deque<T> {
    var enQueue: [T]
    var deQueue: [T] = []
    
    var size: Int {
        return enQueue.count + deQueue.count
    }
    
    var isEmpty: Bool {
        return enQueue.isEmpty && deQueue.isEmpty
    }
    
    init(_ queue: [T]) {
        enQueue = queue
    }
    
    mutating func pushFirst(_ element: T) {
        self.deQueue.append(element)
    }
    
    mutating func pushLast(_ element: T) {
        self.enQueue.append(element)
    }
    
    mutating func popFirst() -> T? {
        if self.deQueue.isEmpty {
            self.deQueue = self.enQueue.reversed()
            self.enQueue.removeAll()
        }
        return self.deQueue.popLast()
    }
    
    mutating func popLast() -> T? {
        if self.enQueue.isEmpty {
            self.enQueue = self.deQueue.reversed()
            self.deQueue.removeAll()
        }
        return self.enQueue.popLast()
    }
}


// TC
let priorities = [2, 1, 3, 2]
let location = 2
print(solution(priorities, location)) // 1
