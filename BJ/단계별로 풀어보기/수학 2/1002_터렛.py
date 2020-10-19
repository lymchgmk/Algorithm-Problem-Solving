import sys
import math
sys.stdin = open('1002_터렛.txt', 'rt')


def dist(X1, X2, Y1, Y2):
    return ((X1 - X2)**2 + (Y1 - Y2)**2)**0.5

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    min_r, max_r = min(r1, r2), max(r1, r2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    else:
        d = dist(x1, x2, y1, y2)
        if min_r + max_r < d or max_r - min_r > d:
            print(0)
        elif min_r + max_r == d or max_r - min_r == d:
            print(1)
        elif max_r - min_r < d < min_r + max_r:
            print(2)
