import sys
sys.stdin = open("12015_가장 긴 증가하는 부분 수열 2.txt", 'rt')


from bisect import bisect_left

input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))

LIS = [0]
for a in A:
    if LIS[-1] < a:
        LIS.append(a)
    else:
        LIS[bisect_left(LIS, a)] = a

print(len(LIS)-1)