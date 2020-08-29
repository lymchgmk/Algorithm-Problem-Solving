import sys
sys.stdin = open("BJ_15685_드래곤 커브.txt")

def dragon_curve(start):
    x, y, d, g = start[0], start[1], start[2], start[3]
    result = []

    if d == 0:
    elif d == 1:
    elif d == 2:
    elif d == 3:

    for i in range(g):



N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
L = len(data)
arr = [[0 for _ in range(101)] for _ in range(101)]


for i in range(L):
    dragon_curve(data[i])

count = 0
for i in range(L):
    for j in range(L):
        if arr[i][j] == 1: # 4점이 다 1이 경우 카운트하기
            count += 1

print(count)



