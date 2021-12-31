import sys
sys.stdin = open('2559_수열.txt', 'r')


input = lambda: sys.stdin.readline().strip()
N, K = map(int, input().split())
T = list(map(int, input().split()))

start = 0
result = sum(T[:K])
tmp = result
while start + K < N:
    tmp -= T[start]
    tmp += T[start + K]
    if result < tmp:
        result = tmp
    start += 1
    
print(result)
