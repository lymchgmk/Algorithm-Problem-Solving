import sys
sys.stdin = open('19237_어른 상어.txt', 'r', encoding='UTF8')

N, M, k = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(N)]
smells = [[0 for _ in range(N)] for _ in range(N)]
are_sharks = [False] * M
for i in range(N):
    for j in range(N):
        if sharks[i][j] != 0:
            smells[i][j] = k
            are_sharks[sharks[i][j]-1] = True
start_dirs = list(map(int, input().split()))
dirs_priority = [list(map(int, input().split())) for _ in range(M)]

t = 0
# while True:
#     if t > 1000:
#         for z in range(N):
#             print(sharks[z])
#         print()
#         for z in range(N):
#             print(smells[z])
#         print()

#         print(-1)
#         break
#     if are_sharks.count(True) == 1:
#         for z in range(N):
#             print(sharks[z])
#         print()
#         for z in range(N):
#             print(smells[z])
#         print()
        
#         print(t)
#         break

#     for z in range(N):
#         print(sharks[z])
#     print()
#     for z in range(N):
#         print(smells[z])
#     print()
        

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
                            # 방향, 상어번호, 전 x좌표, 전 y좌표, 후 x좌표, 후 y좌표
                            no_smell.append([d, picked_shark_idx, i, j, x, y])
                        else:
                            yes_smell.append([d, picked_shark_idx, i, j, x, y])
                # 하
                elif d == 2:
                    x, y = i+1, j
                    if 0<=x<N and 0<=y<N:
                        if smells[x][y] == 0:
                            no_smell.append([d, picked_shark_idx, i, j, x, y])
                        else:
                            yes_smell.append([d, picked_shark_idx, i, j, x, y])
                # 좌
                elif d == 3:
                    x, y = i, j-1
                    if 0<=x<N and 0<=y<N:
                        if smells[x][y] == 0:
                            no_smell.append([d, picked_shark_idx, i, j, x, y])
                        else:
                            yes_smell.append([d, picked_shark_idx, i, j, x, y])
                # 우
                elif d == 4:
                    x, y = i, j+1
                    if 0<=x<N and 0<=y<N:
                        if smells[x][y] == 0:
                            no_smell.append([d, picked_shark_idx, i, j, x, y])
                        else:
                            yes_smell.append([d, picked_shark_idx, i, j, x, y])

            if no_smell:
                moved_shark = no_smell[0]
            else:
                moved_shark = yes_smell[0]

            d, picked_shark_idx, before_x, before_y, after_x, after_y = moved_shark
            start_dirs[picked_shark_idx] = d
            if sharks[after_x][after_y] == 0:
                sharks[before_x][before_y] = picked_shark_idx+1
            else:
                sharks[after_x][after_y] = min(sharks[after_x][after_y], picked_shark_idx+1)
                are_sharks[max(sharks[after_x][after_y], picked_shark_idx+1)-1] = False

            sharks[before_x][before_y] = 0
            smells[after_x][after_y] = k

# 2. 냄새 남기기
for i in range(N):
    for j in range(N):
        if 1 <= smells[i][j] <=k:
            smells[i][j] -= 1

t += 1

for z in range(N):
    print(sharks[z])
print()
for z in range(N):
    print(smells[z])
print()
        