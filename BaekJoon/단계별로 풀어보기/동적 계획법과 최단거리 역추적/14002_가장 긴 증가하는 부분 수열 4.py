import sys
sys.stdin = open("14002_가장 긴 증가하는 부분 수열.txt", 'rt')
import bisect

input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))

dp_A = [A[0]]
dp_LIS = []

for num in A:
    if dp_A[-1] < num:
        dp_A.append(num)
        dp_LIS.append([len(dp_A)-1, num])
    else:
        idx = bisect.bisect_left(dp_A, num)
        dp_A[idx] = num
        dp_LIS.append([idx, num])
        
LIS_idx = len(dp_A) - 1
LIS = []
for i in range(N-1, -1, -1):
    if dp_LIS[i][0] == LIS_idx:
        LIS.append(dp_LIS[i][1])
        LIS_idx -= 1

print(len(LIS))
print(*reversed(LIS))
