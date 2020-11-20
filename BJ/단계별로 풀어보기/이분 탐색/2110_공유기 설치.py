import sys
sys.stdin = open("2110_공유기 설치.txt", 'rt')


input = lambda: sys.stdin.readline().strip()
N, C = map(int, input().split())
HOUSE = list(int(input()) for _ in range(N))
HOUSE.sort()

s, e = 1, (HOUSE[N-1]-HOUSE[0])//(C-1) + 1
answer = 0
while s <= e:
    m = (s+e)//2
    t, cnt = 0, 1
    for i in range(N):
        if HOUSE[i] - HOUSE[t] >= m:
            cnt += 1
            t = i

    if cnt >= C:
        s = m + 1
        answer = max(answer, m)
    else:
        e = m - 1
    
print(answer)