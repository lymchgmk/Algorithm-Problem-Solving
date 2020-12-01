import sys
sys.stdin = open("20303_할로윈의 양아치.txt", "rt")
input = lambda: sys.stdin.readline().strip()


def DFS(adj_list, start):
    visited = []
    stack = [start]

    while stack:
        temp = stack.pop()
        if temp not in visited:
            visited.append(temp)
            stack.extend(adj_list[temp])
    
    return visited


N, M, K = map(int, input().split())
c = list(map(int, input().split()))

adj_list = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

stoled_together = [DFS(adj_list, i) for i in range(1, N+1)]

stoled_candies = []
for st in stoled_together:
    candy_sum = 0
    for kid in st:
        candy_sum += c[kid-1]
    stoled_candies.append((len(st), candy_sum))

stoled_candies = [(0, 0)] + list(set(stoled_candies))
stoled_candies.sort()
L = len(stoled_candies)
dp_ks = [[0]*(K) for _ in range(L)]
for i in range(1, L):
    for j in range(1, K):
        w, v = stoled_candies[i]
        if j < w:
            dp_ks[i][j] = dp_ks[i-1][j]
        else:
            dp_ks[i][j] = max(dp_ks[i-1][j-w] + v, dp_ks[i-1][j])

answer = dp_ks[L-1][K-1]
print(answer)