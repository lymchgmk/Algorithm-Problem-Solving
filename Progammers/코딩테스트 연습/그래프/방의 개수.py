from collections import deque
# 방향 정보 리스트
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
def solution(arrows):
    chck, direc, q = {}, {}, deque()
    chck[(0, 0)] = 0
    q.append([0, 0])
    x, y, ans = 0, 0, 0
    # arrows 방향에 대해 방향정보,방문여부를 딕셔너리 및 큐에 저장
    for i in arrows:
        for j in range(2):
            currx = x + dx[i]
            curry = y + dy[i]
            chck[(currx, curry)] = 0
            direc[(x, y, currx, curry)] = 0
            direc[(currx, curry, x, y)] = 0
            q.append([currx, curry])
            x, y = currx, curry
    x, y = q.popleft()
    chck[(x, y)] = 1
    while q:
        # 현재 위치와 다음 위치에 대한 검사 실시
        nx, ny = q.popleft()
        # 이동할 위치가 방문한 적이 있고
        if chck[(nx, ny)] == 1:
            # 전에 이동을 했던 방향이 아니라면
            if direc[(x, y, nx, ny)] == 0:
                # 답 증가, 해당 구간 이동여부 변경
                ans += 1
                direc[(x, y, nx, ny)] = 1
                direc[(nx, ny, x, y)] = 1
        # 이동할 위치에 방문한적이 없다면
        else:
            # 해당 위치 방문 여부 변경 및 해당 구간 이동여부 변경
            chck[(nx, ny)] = 1
            direc[(x, y, nx, ny)] = 1
            direc[(nx, ny, x, y)] = 1
        # 현재 위치를 이동할 위치였던 좌표로 변경
        x, y = nx, ny
    return ans