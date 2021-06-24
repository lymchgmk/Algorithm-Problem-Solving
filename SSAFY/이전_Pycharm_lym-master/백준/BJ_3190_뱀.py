## 사과 먹으면 없어지는거 고려안해서 오래 걸림

import sys
sys.stdin = open("BJ_3190_뱀.txt")

import collections
# 꼬리는 짧아지거나 안짧아지거나 = FIFO == Queue 사용해서 전체 보드의 좌표 + 머리 좌표로 처리

def issafe(HEAD, BODY):
    if (0<= HEAD[0] <N and 0<=HEAD[1]<N) and (HEAD not in BODY):
        return True
    else:
        return False

def rotate_dir(s, dir):
    if dir == [1, 0]:
        if s == 'L':
            r_dir = [0, 1]
        elif s == 'D':
            r_dir = [0, -1]

    elif dir == [-1, 0]:
        if s == 'L':
            r_dir = [0, -1]
        elif s == 'D':
            r_dir = [0, 1]

    elif dir == [0, 1]:
        if s == 'L':
            r_dir = [-1, 0]
        elif s == 'D':
            r_dir = [1, 0]

    elif dir == [0, -1]:
        if s == 'L':
            r_dir = [1, 0]
        elif s == 'D':
            r_dir = [-1, 0]

    return r_dir


#문제 데이터 받기
N = int(input())

K = int(input())
apple = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
snake_move = [list(map(str, input().split())) for _ in range(L)]
for i in range(L):
    snake_move[i][0] = int(snake_move[i][0])

#보드에 사과 깔기
board = [[0 for _ in range(N)] for _ in range(N)]
for i in range(K):
   board[apple[i][0]-1][apple[i][1]-1] = 1


#초기조건
time = 0
snake_head = [0, 0]
snake_body = collections.deque()
dir = [0, 1]

#뱀 움직이기
while True:#보드 밖에 머리가 나가거나 or 몸에 부딫히거나(=머리 좌표가 몸 좌표 큐에 중복되는 경우
    time += 1

    temp = snake_head.copy()
    snake_body.append(temp)
    snake_head[0] += dir[0]
    snake_head[1] += dir[1]

    if issafe(snake_head, snake_body) is False:
        break

    for i in range(L):
        if snake_move[i][0] == time:
            dir = rotate_dir(snake_move[i][1], dir)

    if issafe(snake_head, snake_body) and board[snake_head[0]][snake_head[1]] == 0:
        snake_body.popleft()

    elif issafe(snake_head, snake_body) and board[snake_head[0]][snake_head[1]] == 1:
        board[snake_head[0]][snake_head[1]] = 0
        continue

# 답 출력
print(time)