def solution(n, s, a, b, fares):
    def floyd_warshall(dist):
        for i in range(n+1):
            for j in range(n+1):
                for k in range(n+1):
                    if j != k and dist[j][k] > dist[j][i] + dist[i][k]:
                        dist[j][k] = dist[j][i] + dist[i][k]
        return dist

    INF = float('inf')
    dist = [[INF] * (n+1) for _ in range(n+1)]
    for fare in fares:
        dep, arr, cost = fare
        dist[dep][arr] = min(dist[dep][arr], cost)
        dist[arr][dep] = min(dist[arr][dep], cost)
    
    dist = floyd_warshall(dist)
    for i in range(1, n+1):
        dist[i][i] = 0
    
    answer = dist[s][a] + dist[s][b]
    for split in range(1, n+1):
        tmp = dist[s][split] + dist[split][a] + dist[split][b]
        answer = min(answer, tmp)
        
    return answer
    

n = 6
s = 4
a = 6
b = 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))
