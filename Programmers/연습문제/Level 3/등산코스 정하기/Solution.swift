import Foundation

func solution(_ n:Int, _ paths:[[Int]], _ gates:[Int], _ summits:[Int]) -> [Int] {
    typealias Node = Int
    typealias Intensity = Int

    //
    var isGate: [Node: Bool] = [:]
    var isSummit: [Node: Bool] = [:]
    (1...n).forEach {
        isGate[$0] = false
        isSummit[$0] = false
    }
    gates.forEach { isGate[$0, default: false] = true }
    summits.forEach { isSummit[$0, default: false] = true}

    //
    var adjList: [Node: [(Node, Intensity)]] = [:]
    paths.forEach { path in
        let (start, end, intensity) = (path[0], path[1], path[2])
        let (startIsGate, endIsGate) = (isGate[start] ?? false, isGate[end] ?? false)
        let (startIsSummit, endIsSummit) = (isSummit[start] ?? false, isSummit[end] ?? false)
        if startIsGate || endIsSummit {
            adjList[start, default: []].append((end, intensity))
        } else if endIsGate || startIsSummit {
            adjList[end, default: []].append((start, intensity))
        } else {
            adjList[start, default: []].append((end, intensity))
            adjList[end, default: []].append((start, intensity))
        }
    }

    // 다익스트라
    let maxIntensity: Intensity = 10_000_000
    var intensities: [Node: Intensity] = [:]
    (1...n).forEach {
        intensities[$0] = maxIntensity
    }
    var queue: [(Node, Intensity)] = gates.map { gate in
        intensities[gate] = 0
        return (gate, 0)
    }
    var index = 0

    while index < queue.count {
        let (currNode, currIntensity) = (queue[index].0, queue[index].1)
        index += 1

        guard let postNodes = adjList[currNode]
        else {
            continue
        }

        postNodes.forEach { (postNode, postIntensity) in
            let intensity = max(currIntensity, postIntensity)

            if intensity < (intensities[postNode] ?? maxIntensity) {
                intensities[postNode] = intensity
                queue.append((postNode, intensity))
            }
        }
    }

    var answer = [n, maxIntensity]
    intensities.forEach { (index, intensity) in
        if (isSummit[index] ?? false) {
            let (currIndex, currIntensity) = (answer[0], answer[1])

            if currIntensity > intensity {
                answer = [index, intensity]
            }

            if currIntensity == intensity && currIndex > index {
                answer = [index, intensity]
            }
        }
    }

    return answer
}

let n = 6
let paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
let gates = [1, 3]
let summits = [5]
print(solution(n, paths, gates, summits)) // [5, 3]