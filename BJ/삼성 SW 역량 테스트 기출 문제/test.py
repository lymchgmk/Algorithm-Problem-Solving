import sys
sys.stdin = open("19238_스타트 택시.txt", "r")


from collections import deque
from copy import deepcopy


# 0. 초기 데이터
N, M, fuel = map(int, input().split())
map_data = [list(-1 if x == 1 else 0 for x in map(int, input().split())) for _ in range(N)]
taxi = list(map(lambda x: x-1, map(int, input().split())))
customers_data = [list(map(lambda x: x-1, map(int, input().split()))) for _ in range(M)]

# 0-1. 내 데이터
is_arrived = [False] * M

# 1. BFS로 거리 측정
def BFS_measure_distance(start, end, map_data):
    distance_map = deepcopy(map_data)
    visited = []

    dir = ((1, 0), (-1, 0), (0, 1), (0, -1))

    deq = deque()
    deq.append(start)

    while deq:

        temp = deq.popleft()

        if temp == end:
            # 1-1. 예외) 연료 부족으로 도달 못함
            if distance_map[temp[0]][temp[1]] > fuel:
                return -1
            else:
                # end에 도달하는 경우
                return distance_map[temp[0]][temp[1]]

<<<<<<< HEAD
        for i in range(4):
            test = (temp[0] + dir[i][0], temp[1] + dir[i][1])

            if 0 <= test[0] < N and 0 <= test[1] < N and map_data[test[0]][test[1]] != -1 and test not in visited:
                distance_map[test[0]][test[1]] = distance_map[temp[0]][temp[1]] + 1
                visited.append(temp)
                deq.append(test)
    
    # 1-2. 예외) 벽때문에 도달 못함
    if distance_map[end[0]][end[1]] == 0: return -1
    else:
        return distance_map[end[0]][end[1]]

flag = False
while False in is_arrived:
    who_can_take_taxi = []
    for i in range(M):
        if is_arrived[i] is False:
            distance = BFS_measure_distance(taxi, customers_data[i][:2], map_data)
            if distance != -1:
                who_can_take_taxi.append([distance] + customers_data[i] + [i])
    
    if not who_can_take_taxi:
        flag = True
        break

    if flag == True:
        break

    who_takes_taxi = sorted(who_can_take_taxi, key = lambda x : (x[0], x[1], x[2]))[0]
    fuel -= who_takes_taxi[0]
    taxi = who_takes_taxi[1:3]

    arrival_distance = BFS_measure_distance(taxi, who_takes_taxi[3:5], map_data)
    if fuel < arrival_distance or arrival_distance == -1:
        flag = True
        break

    fuel += arrival_distance
    taxi = who_takes_taxi[3:5]
    is_arrived[who_takes_taxi[-1]] = True

if flag == False:
    print(fuel)
else:
    print(-1)
=======
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
>>>>>>> 971b1f6e451e2f7faab3cd941bfa958690789bb7
