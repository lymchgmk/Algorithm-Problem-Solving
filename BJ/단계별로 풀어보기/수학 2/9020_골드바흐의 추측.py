import sys
sys.stdin = open('9020_골드바흐의 추측.txt', 'rt')


flag = [True] * 10000
for i in range(2, 100):
    for j in range(2 * i, 10000, i):
        flag[j] = False

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n//2, 1, -1):
        if flag[i] and flag[n-i]:
            print(i, n-i)
            break
