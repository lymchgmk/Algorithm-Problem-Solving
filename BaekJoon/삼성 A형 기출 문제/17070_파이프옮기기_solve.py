import sys
sys.stdin=open('17070_파이프옮기기.txt')

N = int(input())
my_map = [[0]* (N + 1)]  + [[0] + list(map(int, input().split())) for _ in range(N)]
cnts = [[[0] * 3 for _ in range(N + 1)] for _ in range(N + 1)]
cnts[1][2][0] = 1
for r in range(1, 1 + N):
    for c in range(1, 1 + N):
        if not my_map[r][c]:
            cnts[r][c][0] += cnts[r][c-1][0] + cnts[r][c-1][1]  # 가로
            cnts[r][c][2] += cnts[r-1][c][2] + cnts[r-1][c][1]  # 세로
            if not my_map[r-1][c] and not my_map[r][c-1]:
                for i in range(3):
                    cnts[r][c][1] += cnts[r-1][c-1][i]  # 대각선

print(sum(cnts[r][c]))