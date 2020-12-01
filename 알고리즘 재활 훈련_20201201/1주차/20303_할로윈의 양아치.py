import sys
sys.stdin = open("20303_할로윈의 양아치.txt", "rt")
input = lambda: sys.stdin.readline().strip()


def DFS(start):
    global dfs_visited
    dfs_visited.append(start)
    for next in adj_list[start]:
        if next not in dfs_visited:
            DFS(next)


N, M, K = map(int, input().split())
c = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]

adj_list = [[] for _ in range(N+1)]
for ab in AB:
    a, b = ab
    adj_list[a].append(b)
    adj_list[b].append(a)

stoled_together = []
for i in range(1, N+1):
    dfs_visited = []
    DFS(i)
    stoled_together.append(dfs_visited)

stoled_candies = []
for st in stoled_together:
    candy_sum = 0
    for kid in st:
        candy_sum += c[kid-1]
    stoled_candies.append((len(st), candy_sum))

stoled_candies = [(0, 0)] + list(set(stoled_candies))
stoled_candies.sort()
L = len(stoled_candies)
dp_ks = [[0]*K for _ in range(L)]
for i in range(1, L):
    for j in range(1, K):
        w, v = stoled_candies[i]
        if j < w:
            dp_ks[i][j] = dp_ks[i-1][j]
        else:
            dp_ks[i][j] = max(dp_ks[i-1][j-w] + v, dp_ks[i-1][j])

print(dp_ks[L-1][K-1])