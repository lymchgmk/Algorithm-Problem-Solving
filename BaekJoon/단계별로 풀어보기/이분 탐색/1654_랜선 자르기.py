import sys
sys.stdin = open("1654_랜선 자르기.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
K, N = map(int, input().split())
LAN = [int(input()) for _ in range(K)]
s, e = 1, max(LAN)

while s <= e:
    m = (s+e)//2
    cnt = sum([lan//m for lan in LAN])

    if cnt >= N:
        s = m + 1
    else:
        e = m - 1

print(e)