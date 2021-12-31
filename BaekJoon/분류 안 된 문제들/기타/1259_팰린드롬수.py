import sys
sys.stdin = open('1259_팰린드롬수.txt', 'r')
input = lambda: sys.stdin.readline().strip()


while True:
    P = input()
    if P == '0':
        break
    else:
        L = len(P)
        dp = [[0]*L for _ in range(L)]

        for i in range(L):
            dp[i][i] = 1
        
        for i in range(L-1):
            if P[i] == P[i+1]:
                dp[i][i+1] = 1
        
        for i in range(2, L):
            for j in range(L-i):
                if P[j] == P[j+i] and dp[j+1][j+i-1] == 1:
                    dp[j][j+i] = 1

        if dp[0][L-1]:
            print('yes')
        else:
            print('no')