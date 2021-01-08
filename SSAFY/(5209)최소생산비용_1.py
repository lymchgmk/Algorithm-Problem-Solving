import time
start = time.time()
def perm(n, k, cursum):
    global min
    if min <= cursum : return

    if n == k:
        if cursum < min: min = cursum
    else:
        for i in range(k, n):
            A[i], A[k] = A[k], A[i]
            perm(n, k+1, cursum + data[k][A[k]])
            A[i], A[k] = A[k], A[i]

import sys
sys.stdin = open("(5209)최소생산비용_input.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    A = list(range(N))
    min = 987654321
    perm(N, 0, 0)
    print('#{} {}'.format(tc+1, min))

print("{} seconds".format(time.time()-start))