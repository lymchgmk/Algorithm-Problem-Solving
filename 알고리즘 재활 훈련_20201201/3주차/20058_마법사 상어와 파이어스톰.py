import sys
sys.stdin = open('20058_마법사 상어와 파이어스톰.txt', 'rt')
input = lambda: sys.stdin.readline().strip()


def firestorm(ice_area, n, how_many_fs, divide_len):
    def divide_and_rotate(divide_len):
        for i in range(0, 2**n, 2**divide_len):
            for j in range(0, )

    def melt():
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for x in range(2**n):
            for y in range(2**n):
                for d in dirs:
                    nx = 

    
    for dl in divide_len:
        divide_and_rotate(dl)
        melt()

    return ice_area


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

A = firestorm(A, N, Q, L)

sum_ice, max_ice = 0, 0
for i in range(2**N):
    for j in range(2**N):
        ice = A[i][j]
        sum_ice += ice
        max_ice = max(ice, max_ice)

print(sum_ice)
print(max_ice)