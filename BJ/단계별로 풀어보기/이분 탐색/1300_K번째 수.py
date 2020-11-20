import sys
sys.stdin = open("1300_K번째 수.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
k = int(input())

s, e = 1, k
while s <= e:
    m = (s+e)//2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(m//i, N)
    
    if cnt < k:
        s = m + 1
    else:
        e = m - 1

print(s)