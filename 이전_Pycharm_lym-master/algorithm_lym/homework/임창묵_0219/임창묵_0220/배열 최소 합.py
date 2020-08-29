import sys
sys.stdin = open("배열 최소 합.txt")

import itertools

# 1에서 N 짜리 리스트를 만들고, 순열을 돌려서, 각 행마다 곱해서 더하자.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    prmt_N_list = itertools.permutations(list(range(N)), N)

    result = 10*N
    for prmt_N in prmt_N_list:
        sum = 0
        for i in range(N):
            sum += arr[i][prmt_N[i]]
            if sum >= result:
                break # 가지치기

        if sum < result:
            result = sum

    print("#{} {}".format(test_case, result))