import sys
sys.stdin = open('14003_가장 긴 증가하는 부분 수열 5.txt', 'rt')
import bisect


def my_bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid= (lo+hi)//2
        if a[mid] < x:
            lo= mid+1
        else:
            hi = mid
    return lo


input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

dp_A = [A[0]]
dp_LIS= []

for num in A:
    if dp_A[-1] < num:
        dp_A.append(num)
        dp_LIS.append([len(dp_A) - 1, num])
    else:
        change_idx = my_bisect_left(dp_A, num)
        # change_idx = bisect.bisect_left(dp_A, num)
        dp_A[change_idx] = num
        dp_LIS.append([change_idx, num])
        
LIS = []
LIS_idx = len(dp_A) - 1
for i in range(N-1, -1, -1):
    if dp_LIS[i][0] == LIS_idx:
        LIS.append(dp_LIS[i][1])
        LIS_idx -= 1
LIS.reverse()

print(len(LIS))
print(*LIS)
