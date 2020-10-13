import sys
sys.stdin = open('19236_아기 상어.txt', 'rt')

N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]

fishes=[]
for i in range(N):
    for j in range(N):
        if 0 <= sea[i][j] <= 6: fishes.append([i, j, sea[i][j]])
        elif sea[i][j] == 9: baby_shark = [i, j, 2]

t = 0
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
while fishes:
    can_eat = []
    for d in dirs:
        x, y = baby_shark[0] + d[0], baby_shark[1] + d[1]
        if 0<=x<N and 0<=y<N and sea[x][y] <= baby_shark[2]:
            can_eat.append([x, y, sea[x][y]])
    
    if not can_eat:
        break
    

print(t)

    
            
    

