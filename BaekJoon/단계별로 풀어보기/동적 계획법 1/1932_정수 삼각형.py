import sys
sys.stdin = open("1932_정수 삼각형.txt", 'rt')

input = sys.stdin.readline
n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

dp = t[0]
s, e = t[0][0], t[0][0]
for i in range(1, n):
    s += t[i][0]
    e += t[i][i]
    temp = [t[i][j] + max(dp[j-1], dp[j]) for j in range(1, i)]
    dp = [s] + temp + [e]
print(max(dp))
