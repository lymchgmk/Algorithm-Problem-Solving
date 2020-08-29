import sys
sys.stdin = open('4613. 러시아 국기 같은 깃발.txt', 'r')

from itertools import combinations_with_replacement

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    data = [list(input()) for _ in range(N)]
    # print(data)

    # White, Blue, Red
    russian_flag = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if data[i][j] == 'W': russian_flag[i][0] += 1
            if data[i][j] == 'B': russian_flag[i][1] += 1
            if data[i][j] == 'R': russian_flag[i][2] += 1
    # print(test_case, russian_flag)

    comb = combinations_with_replacement(list(range(1, N-1)), 2)

    result = N * M
    for c in comb:
        sample = (M - russian_flag[0][0]) + (M - russian_flag[N-1][2])
        for i in range(1, N-1):
            if i < c[0]: sample += (M - russian_flag[i][0])
            if  c[0] <= i < c[1]+1: sample += (M - russian_flag[i][1])
            if c[1] < i: sample += (M - russian_flag[i][2])
        if result > sample: result = sample

    print(f'#{test_case} {result}')