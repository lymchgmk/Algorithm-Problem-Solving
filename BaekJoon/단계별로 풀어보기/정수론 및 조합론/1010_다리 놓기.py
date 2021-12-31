import sys
sys.stdin = open('1010_다리 놓기.txt', 'rt')


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    answer = 1
    K = M - N
    while M > K:
        answer *= M
        M -= 1
    while N:
        answer //= N
        N -= 1
    
    print(answer)