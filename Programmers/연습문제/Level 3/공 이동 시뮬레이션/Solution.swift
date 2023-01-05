import Foundation

func solution(_ n: Int, _ m: Int, _ x: Int, _ y: Int, _ queries: [[Int]]) -> Int64 {
    let (n, m, x, y) = (Int64(n), Int64(m), Int64(x), Int64(y))
    var point = [y, y+1, x, x+1]
    let dir = [Int64(-1), Int64(1), Int64(-1), Int64(1)]
    let boundary = [0, m, 0, n]
    let limit = [m, m, n, n]

    for query in queries.reversed() {
        let (command, dx) = (query[0], Int64(query[1]))
        let reverse = command ^ 1

        point[reverse] += dir[reverse] * dx
        point[reverse] = max(min(point[reverse], limit[reverse]), 0)

        if point[command] != boundary[command] {
            point[command] += dir[reverse] * dx
            point[command] = max(min(point[command], limit[command]), 0)
        }

        if point[0] == m || point[1] == 0 || point[2] == n || point[3] == 0 {
            return Int64(0)
        }
    }

    return (point[1] - point[0]) * (point[3] - point[2])
}