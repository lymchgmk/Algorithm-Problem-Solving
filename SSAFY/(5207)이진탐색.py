def binarySearch(a, key):
    low = 0
    high = len(a)-1
    dir = -1                    # 방향 미정, 왼쪽:0, 오른쪽: 1
    while low <= high:
        mid = (low + high) // 2
        if key == a[mid]:           # 찾았을 때
            return 1
        elif key < a[mid]:      # 왼쪽 방향
            if dir == 0:            # 같은 왼쪽일 때 -> 중단
                return 0
            else:
                high = mid - 1
                dir = 0
        else:                   # 오른쪽 방향
            if dir == 1:            # 같은 오른쪽일 때 -> 중단
                return 0
            else:
                low = mid + 1
                dir = 1
    return 0

import sys
sys.stdin = open('(5207)이진탐색_input.txt', 'r')
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for i in range(M):
        cnt += binarySearch(A, B[i])
    print("#{} {}".format(tc+1, cnt))
