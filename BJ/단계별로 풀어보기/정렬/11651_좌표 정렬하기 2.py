import sys
sys.stdin = open('11651_좌표 정렬하기 2.txt', 'rt')


def input():
    return sys.stdin.readline().strip()

N = int(input())
P = sorted([list(map(int, input().split())) for _ in range(N)], key = lambda x: (x[1], x[0]))
for x, y in P:
    print(x, y)