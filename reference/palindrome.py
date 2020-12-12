sample = input()
L = len(sample)

dp = [[0]*L for _ in range(L)]

# palindrome의 길이가 1인 경우
for i in range(L):
    dp[i][i] = 1

# palindrome의 길이가 2인 경우
for i in range(L-1):
    if sample[i] == sample[i+1]:
        dp[i][i+1] = 1

# palindrome의 길이가 3이상인 경우
for i in range(2, N):
    for j in range(N-i):
        if sample[j] == sample[]
