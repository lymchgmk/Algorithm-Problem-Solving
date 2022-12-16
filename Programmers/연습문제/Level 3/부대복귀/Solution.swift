import Foundation

func solution(_ n:Int, _ roads:[[Int]], _ sources:[Int], _ destination:Int) -> [Int] {

    var adjMatrix: [Int: [(Int, Int)]] = [:]
    var dist: [Int: Int] = [:]
    roads.forEach { road in
        if let start = road.first,
           let end = road.last {
              adjMatrix[start, default: []].append((end, 1))
              adjMatrix[end, default: []].append((start, 1))
        }
    }

    var queue: [(Int, Int)] = [(destination, 0)]
    var index = 0
    var visited = Array(repeating: false, count: n+1)
    visited[destination] = true

    while index < queue.count {
        let (currNode, currDist) = (queue[index].0, queue[index].1)
        index += 1
        dist[currNode] = currDist

        guard let postNodes = adjMatrix[currNode]
        else {
            dist[currNode] = -1
            continue
        }

        postNodes.forEach { (postNode, postDist) in
            if !visited[postNode] {
                visited[postNode] = true
                queue.append((postNode, currDist + postDist))
            }
        }
    }

    return sources.map { dist[$0] ?? -1 }
}

let n = 3
let roads = [[1, 2], [2, 3]]
let sources = [2, 3]
let destination = 1
print(solution(n, roads, sources, destination)) // [1, 2]