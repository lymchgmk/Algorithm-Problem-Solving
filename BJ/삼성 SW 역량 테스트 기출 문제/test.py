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