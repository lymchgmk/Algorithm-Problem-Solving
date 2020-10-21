import sys
sys.stdin = open('9375_패션왕 신해빈.txt', 'rt')


T = int(input())
for _ in range(T):
    N = int(input())
    clothes = []
    for _ in range(N):
        clothes.append(list(input().split()))

    print(N, clothes)