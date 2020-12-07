import sys
sys.stdin = open('20056_마법사 상어와 파이어볼.txt', 'rt')
input = lambda: sys.stdin.readline().strip()
from collections import deque


def FB_move():
    for i in range(N):
        for j in range(N):
            if MAP[i][j] != None and MAP[i][j][0] == False:
                pass
    
    for i in range(N):
        for j in range(N):
            if len(MAP[i][j]) > 1:



N, M, K = map(int, input().split())
MAP = [[None]*N for _ in range(N)]
for _ in range(M):
    fb = list(map(int, input().split()))
    MAP[fb[0]-1][fb[1]-1] = [False] + fb[2:]
print(MAP)