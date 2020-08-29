import sys
sys.stdin = open('4041_활주로 건설.txt', 'r')

T = int(input())

for test_case in range(1, T+1):
    N, X = map(int, input().split()) #N: 행렬 크기 / X: 높이 1인 경사로의 길이
    land = []
    for ground in range(N):
        land.append(list(map(int, input().split())))
#
    land_row = land
    land_column = []
    for i in range(N):
        land_column.append([row[i] for row in land])
#

#메커니즘 생각이 안됨
    # for i in range(N):
    #     for j in range(N):
    #         land_row[i][j]
    #         land_column[i][j]