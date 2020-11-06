import sys
sys.stdin = open('10814_나이순 정렬.txt', 'rt')


def input():
    return sys.stdin.readline().strip()


N = int(input())
W = sorted([input().split() for i in range(N)], key = lambda x: int(x[0]))
for w in W:
    print(*w)