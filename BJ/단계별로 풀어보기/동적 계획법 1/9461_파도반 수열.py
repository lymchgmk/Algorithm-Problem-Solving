import sys
sys.stdin = open('9461_파도반 수열.txt', 'rt')


def P(n):
    global DP
    start = len(DP)
    while True:
        if n <= len(DP):
            return DP[n-1]
        DP.append(DP[start-2] + DP[start-3])
        start += 1


T = int(input())
DP = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12]
for _ in range(T):
    N = int(input())
    print(P(N))