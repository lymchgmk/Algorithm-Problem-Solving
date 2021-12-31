import sys
sys.stdin = open("12015_가장 긴 증가하는 부분 수열 2.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))

LIS = [0]
for i in range(N):
    low, high = 0, len(LIS)-1
    while low <= high:
        mid = (low+high)//2
        if LIS[mid] < A[i]:
            low = mid+1
        else:
            high = mid-1

    if low >= len(LIS):
        LIS.append(A[i])
    else:
        LIS[low] = A[i]

print(len(LIS)-1)

