import sys
sys.stdin = open('20058_마법사 상어와 파이어스톰.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


def firestorm(ice_area, n, how_many_fs, divide_len):
    def divide_and_rotate(dl):
        L = 2**dl
        rotated_ice_area = [[0]*(2**n) for _ in range(2**n)]
        for i in range(0, 2**n, L):
            for j in range(0, 2**n, L):
                for r in range(L):
                    for c in range(L):
                        rotated_ice_area[i+c][j+L-1-r] = ice_area[i+r][j+c]

        return rotated_ice_area


    def melt(rotated_ice_area):
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        melt_target = [[0]*(2**n) for _ in range(2**n)]
        for x in range(2**n):
            for y in range(2**n):
                for d in dirs:
                    nx, ny = x+d[0], y+d[1]
                    if 0<=nx<2**n and 0<=ny<2**n and rotated_ice_area[nx][ny]:
                        melt_target[x][y] += 1
        
        for x in range(2**n):
            for y in range(2**n):
                if melt_target[x][y] < 3 and rotated_ice_area[x][y]:
                    rotated_ice_area[x][y] -= 1
        
        return rotated_ice_area

    
    for dl in divide_len:
        ice_area = melt(divide_and_rotate(dl))

    return ice_area


def bfs_find_bigest_ice(ice_area):
    bigest_ice_size = 0
    visited = []
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    L = len(ice_area)
    for x in range(L):
        for y in range(L):
            ice_size = 0
            if ice_area[x][y] and [x, y] not in visited:
                ice_size += 1
                deq = deque()
                deq.append([x, y])
                visited.append([x, y])
                while deq:
                    now_x, now_y = deq.popleft()
                    for d in dirs:
                        next_x, next_y = now_x + d[0], now_y + d[1]
                        if 0<=next_x<L and 0<=next_y<L and ice_area[next_x][next_y] and [next_x, next_y] not in visited:
                            ice_size += 1
                            visited.append([next_x, next_y])
                            deq.append([next_x, next_y])
            bigest_ice_size = max(bigest_ice_size, ice_size)

    return bigest_ice_size


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

A = firestorm(A, N, Q, L)

sum_ice = 0
for i in range(2**N):
    sum_ice += sum(A[i])
print(sum_ice)

print(bfs_find_bigest_ice(A))