import sys
sys.stdin = open("BJ_17406_배열 돌리기 4.txt", "r")

import itertools

#1. 90도 회전 함수 정의해서 만들기
#2. permutation, 왜냐하면 6 이하니까 가능할듯
#3. sum(row)로 아니다 싶으면 바로 다음 케이스로 넘기기

def rotate_90 (arr, r, c, s):
    result = [[0 for _ in range(c)] for _ in range(r)]
    std = s
    while std != 0:
        for i in range(r-std-1, r+std):
            for j in range(c-std-1, c+std):
                if i == r-std-1:
                    result[j][c-std-1] = arr[r-std-1][j]
                elif i == r+std-1:
                    result[j][r+std-1] = arr[r+std-1][j]
                elif (i != r-std-1 or i != r+std-1) and j == c-std-1:
                        result[c-std-1][c - j - 1] = arr[i][c-std-1]
                elif (i != r-std-1 or i != r+std-1) and j == c+std-1:
                    result[c+std-1][c - j - 1] = arr[i][c+std-1]
        std -= 1
    return result


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for N_case in range(N)]

r = []
c = []
s = []
for K_case in range(K):
    temp_r, temp_c, temp_s = map(int, input().split())
r.append(temp_r)
c.append(temp_c)
s.append(temp_s)

perm = list(itertools.permutations(list(range(1, K+1))))
print(perm)

for p in range(len(perm)):
    for pp in range(perm[p]):
