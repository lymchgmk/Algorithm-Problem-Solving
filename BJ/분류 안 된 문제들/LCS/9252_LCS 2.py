import sys
sys.stdin= open('9252_LCS 2.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
X = input()
Y = input()

dp = [[0 for i in range(len(X) + 1)] for j in range(len(Y) + 1)]

for i in range(1, len(Y) + 1):
    for j in range(1, len(X) + 1):
        if X[j - 1] == Y[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

LCS = ''
LCS_idx = dp[-1][-1]
y = len(Y)
x = len(X)
while LCS_idx != 0:
    if dp[y][x - 1] == dp[y - 1][x] == LCS_idx - 1:
        LCS = X[x - 1] + LCS
        LCS_idx -= 1
        y -= 1
        x -= 1
    else:
        if dp[y - 1][x] > dp[y][x - 1]:
            y -= 1
        else:
            x -= 1

print(len(LCS))
print(LCS)
