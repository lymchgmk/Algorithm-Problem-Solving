import sys
sys.stdin = open("(1493)수의 새로운 연산_input.txt")
memo = [[0 for _ in range(300)] for _ in range(300)]
x, y = 1, 1
cnt = 1
dic = {}
while cnt <= 40500:
    memo[y][x] = cnt
    dic[cnt] = [x, y]
    if y == 1:  # 맨 아래쪽이면
        y = x + 1
        x = 1
    else:
        y -= 1
        x += 1
    cnt += 1

T = int(input())
for t in range(1, T + 1):
    p, q = map(int, input().split())
    result = memo[dic[p][1] + dic[q][1]][dic[p][0] + dic[q][0]]
    print('#{} {}'.format(t, result))
