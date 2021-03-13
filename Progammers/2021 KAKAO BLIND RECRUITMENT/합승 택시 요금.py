import collections


def solution(n, s, a, b, fares):
    def floyd_warshall():
        for i in range(1, n+1):
            for j in range(1, n+1):
                for k in range(1, n+1):
                    if j != k and dist[j][k] > dist[j][i] + dist[i][k]:
                        dist[j][k] = dist[j][i] + dist[i][k]
        return dist

    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    for s, e, c in fares:
        dist[s][e] = min(dist[s][e], c)

    dist = floyd_warshall()
    for i in range(1, n+1):
        print(dist[i])

    answer = dist[s][a] + dist[s][b]
    for sep in range(1, n+1):
        answer = min(answer, dist[s][sep] + (dist[sep][a] + dist[sep][b]))
    
    return answer


n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
