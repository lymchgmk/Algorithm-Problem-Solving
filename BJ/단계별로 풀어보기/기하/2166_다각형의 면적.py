import sys
import math
sys.stdin = open('2166_다각형의 면적.txt')
input = lambda: sys.stdin.readline().strip()


N = int(input())
points = [list(map(float, input().split())) for _ in range(N)]
points.append(points[0])
res_x, res_y = 0, 0
for i in range(N):
    res_x += points[i][0] * points[i+1][1]
    res_y += points[i][1] * points[i+1][0]
res = round(math.fabs((res_x - res_y) / 2), 1)
print(res)