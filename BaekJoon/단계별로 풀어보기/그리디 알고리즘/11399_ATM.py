import sys
sys.stdin = open('11399_ATM.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
P = list(map(int, input().split()))
result, temp = [], 0
for p in sorted(P):
    temp += p
    result.append(temp)
print(sum(result))