import sys
sys.stdin= open('9251_LCS.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
X = input()
Y = input()

LCS_dp = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
for i, x in enumerate(X):
    for j, y in enumerate(Y):
        if x == y:
            LCS_dp[i+1][j+1] = LCS_dp[i][j] + 1
        else:
            LCS_dp[i+1][j+1] = max(LCS_dp[i+1][j], LCS_dp[i][j+1])

result = ''
j = len(Y)
for i in range(1, len(X)+1):
    if LCS_dp[i][j] != LCS_dp[i-1][j]:
        result += X[i-1]
        
print(len(result))
