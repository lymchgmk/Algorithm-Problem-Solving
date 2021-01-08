import time
start = time.time()

def perm(n, r, k, cursum):
    global min
    if min <= cursum : return

    if r == k:
        if cursum < min: min = cursum
    else:
        for i in range(n):
            if visited[i]: continue
            T[k] = A[i]
            visited[i] = 1
            perm(n, r, k+1, cursum + data[k][T[k]])
            visited[i] = 0


import sys
sys.stdin = open("(5209)최소생산비용_input.txt", "r")
T = int(input())
for tc in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    A = list(range(N))
    T = [0] * N
    visited = [0] * N
    min = 987654321
    perm(N, N,0, 0)
    print('#{} {}'.format(tc+1, min))

print("{} seconds".format(time.time()-start))