import sys
sys.stdin = open('11650_좌표 정렬하기.txt', 'rt')


N = int(input())
P = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: (x[0], x[1]))
for x, y in P:
    print(x, y)