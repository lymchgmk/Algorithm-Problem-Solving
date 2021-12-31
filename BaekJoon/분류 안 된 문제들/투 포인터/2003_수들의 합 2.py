import sys
sys.stdin = open('2003_수들의 합 2.txt', 'r')


input = lambda: sys.stdin.readline().strip()
N, M = map(int, input().split())
A = list(map(int, input().split()))

end = 0
partial_sum = 0
cnt = 0

for start in range(N):
    while partial_sum < M and end < N:
        partial_sum += A[end]
        end += 1
    
    if partial_sum == M:
        cnt += 1
    partial_sum -= A[start]

print(cnt)


