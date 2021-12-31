import sys
sys.stdin = open('1931_회의실배정.txt', 'rt')


input = lambda: sys.stdin.readline().strip()
N = int(input())
meeting = [list(map(int, input().split())) for _ in range(N)]
meeting.sort(key = lambda x: (x[1], x[0]))

answer, temp = 0, 0
for m in meeting:
    if temp <= m[0]:
        answer += 1
        temp = m[1]
print(answer)