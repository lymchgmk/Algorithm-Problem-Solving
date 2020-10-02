import sys
sys.stdin = open("19238_스타트 택시.txt", "r")

from collections import deque

N, M, fuel = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(lambda x: x-1 ,map(int, input().split())))
passenger_data = [list(map(lambda x: x-1 ,map(int, input().split()))) for _ in range(M)]

for i in range(N):
    for j in range(N):
        if map_data[i][j] == 1: map_data[i][j] = -1;

for k in range(M):
    depart, arrive = passenger_data[k][:2], passenger_data[k][2:]
    map_data[depart[0]][depart[1]] = arrive
    

def bfs_taketaxi(start, map_data):
    if type(map_data[start[0]][start[1]]) == list:
        return [0] + start + map_data[start[0]][start[1]]

    # 좌, 상, 우, 하
    dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))

    deq = deque()
    deq.append(start)

    visited = []

    while deq:
        temp_x, temp_y = deq.popleft()

        for dir in dirs:
            test_x, test_y = temp_x + dir[0], temp_y + dir[1]

            if 0 <= test_x < N and 0 <= test_y < N and [test_x, test_y] not in visited:
                if type(map_data[test_x][test_y]) == list:
                    return [map_data[temp_x][temp_y] + 1, test_x, test_y] + map_data[test_x][test_y]
                if type(map_data[test_x][test_y]) == int and map_data[test_x][test_y] != -1:
                    map_data[test_x][test_y] = map_data[temp_x][temp_y] + 1
                    deq.append([test_x, test_y])
                    visited.append([test_x, test_y])

    return -1


def bfs_ridetaxi(taxi, wanna_go, map_data):
    if map_data[taxi[0]][taxi[1]] == wanna_go:
        return 0
    # 좌, 상, 우, 하
    dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))

    deq = deque()
    deq.append(taxi)

    visited = []

    recover = []

    while deq:
        temp_x, temp_y = deq.popleft()

        for dir in dirs:
            test_x, test_y = temp_x + dir[0], temp_y + dir[1]

            if 0 <= test_x < N and 0 <= test_y < N and [test_x, test_y] not in visited:
                if test_x == wanna_go[0] and test_y == wanna_go[1]:
                    for r in recover:
                        map_data[r[0]][r[1]] = r[2]
                    map_data[test_x][test_y] = 0
                    return [map_data[temp_x][temp_y] + 1, test_x, test_y]

                if map_data[test_x][test_y] != -1:
                    if type(map_data[test_x][test_y]) == list:
                        recover.append([test_x, test_y, map_data[test_x][test_y]])
                    map_data[test_x][test_y] = map_data[temp_x][temp_y] + 1
                    deq.append([test_x, test_y])
                    visited.append([test_x, test_y])

    return -1

is_arrived = 0
flag = False
while is_arrived != M:
    passenger = bfs_taketaxi(taxi, map_data)
    if passenger == -1:
        flag = True
        break
    else:
        distance, taxi, wanna_go = passenger[0], passenger[1:3], passenger[3:]
        if distance > fuel:
            flag = True
            break
        map_data[taxi[0]][taxi[1]] = 0
        fuel -= distance
        
    lets_ride = bfs_ridetaxi(taxi, wanna_go, map_data)
    if lets_ride == -1:
        flag = True
        break
    else:
        distance = lets_ride[0]
        if distance > fuel:
            flag = True
            break
        else:
            taxi = lets_ride[1:]
            fuel += distance
    is_arrived += 1

if flag == True:
    print(-1)
else:
    print(fuel)