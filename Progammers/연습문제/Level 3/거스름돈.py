def solution(n, money):
    answer = 0
    return answer


n = 5
money = [1, 2, 5]
print(solution(n, money))


import sys
sys.stdin = open("12865_평범한 배낭.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())
stuff = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]


dp_ks = [[0]*(K+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, K+1):
        w, v = stuff[i]
        if j < w:
            dp_ks[i][j] = dp_ks[i-1][j]
        else:
            dp_ks[i][j] = max(dp_ks[i-1][j-w] + v, dp_ks[i-1][j])

print(dp_ks[N][K])