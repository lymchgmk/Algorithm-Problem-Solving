import sys
sys.stdin = open('19237_어른 상어.txt', 'r', encoding='UTF8')

N, M, k = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(N)]
smells = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if sharks[i][j] != 0:
            smells[i][j] = k
start_dirs = list(map(int, input().split()))
dirs_priority = [list(map(int, input().split())) for _ in range(M)]

# 1. 이동

for i in range(N):
    for j in range(N):
        if sharks[i][j] != 0:
            picked_shark_idx = sharks[i][j]-1
            now_dir = start_dirs[picked_shark_idx]-1
            picked_shark_dirs = dirs_priority[now_dir]
            no_smell, yes_smell = [], []
            for d in picked_shark_dirs:
                # 상
                if d == 1:
                    x, y = i-1, j
                    if 0<=x<N and 0<=y<N:
                        if smells[x][y] == 0:
                            no_smell.append([d,x,y])
                        else:
                            yes_smell.append([d,x,y])
                # 하
                elif d == 2:
                    x, y = i+1, j
                    if 0<=x<N and 0<=y<N:
                        if smells[x][y] == 0:
                            no_smell.append([d,x,y])
                        else:
                            yes_smell.append([d,x,y])
                # 좌
                elif d == 3:
                    x, y = i, j-1
                    if 0<=x<N and 0<=y<N:
                        if smells[x][y] == 0:
                            no_smell.append([d,x,y])
                        else:
                            yes_smell.append([d,x,y])
                # 우
                elif d == 4:
                    x, y = i, j+1
                    if 0<=x<N and 0<=y<N:
                        if smells[x][y] == 0:
                            no_smell.append([d,x,y])
                        else:
                            yes_smell.append([d,x,y])

            if no_smell is True:
                picked_dir = no_smell[0]
                print(picked_dir)

# 2. 냄새 남기기
# 3. 겹치는 상어 없애기
# 4. 방향 결정

 