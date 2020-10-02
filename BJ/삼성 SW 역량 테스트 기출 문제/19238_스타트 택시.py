import sys
sys.stdin = open("19238_스타트 택시.txt", "r")


from collections import deque
from copy import deepcopy


# 초기 데이터
N, M, fuel = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if map_data[i][j] == 1: map_data[i][j] = -1
taxi = list(map(lambda x: x-1, map(int, input().split())))
customers_data = sorted([list(map(lambda x: x-1, map(int, input().split()))) for _ in range(M)], key = lambda x : (x[0], x[1]))


# 함수
def is_safe(start, test_map_data):
    L, x, y = len(map_data), start[0], start[1]
    return 0 <= x < L and 0 <= y < L and test_map_data[x][y] != -1


# 거리 측정하는 함수
def measure_distance(start, end, map_data):
    distance_map = deepcopy(map_data)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    deq = deque()
    deq.append(start)

    while deq:
        temp = deq.popleft()
        x, y = temp[0], temp[1]
        
        if x == end[0] and y == end[1]: 
            return distance_map[x][y]

        for i in range(4):
            test_x, test_y = x + dx[i], y + dy[i]
            test = [test_x, test_y]

            if 0 <= test_x < N and 0 <= test_y < N:
                if distance_map[test_x][test_y] != -1 and distance_map[test_x][test_y] == 0:
                    distance_map[test_x][test_y] = distance_map[x][y] + 1
                    if distance_map[test_x][test_y] > fuel:
                        return -1
                    deq.append(test)


# 내 데이터
is_arrived = [False] * M
customers_distance = [-1] * M
flag = False
count = 0

while count < M:
    # 최소거리 손님 탐색
    for i in range(M):
        if not is_arrived[i]:
            customer = customers_data[i]
            where_is_customer = customer[:2]
            d = measure_distance(taxi, where_is_customer, map_data)
            if d == -1: 
                flag = True
                break

            customers_distance[i] = measure_distance(taxi, where_is_customer, map_data)
        else:
            customers_distance[i] = float('INF')

    if flag == True:
        break

    for i, d in enumerate(customers_distance):
        min_d = min(customers_distance)
        if min_d != -1:
            # 손님 태움
            if d == min_d and d < fuel:
                who_takes_taxi, arrival_location, taxi = i, customers_data[i][2:], customers_data[i][:2]
                fuel -= d
                break
        else:
            flag = True
            break
    if flag == True:
        break

    # 도착지까지 갈 수 있나?
    destination_distance = measure_distance(taxi, arrival_location, map_data)
    if destination_distance == -1:
        flag = True
        break

    if destination_distance <= fuel:
        fuel -= destination_distance
        is_arrived[who_takes_taxi] = True
        taxi = arrival_location
        fuel += 2 * destination_distance
    else:
        flag = True
        break

    count += 1

if flag is True: result = -1
else: result = fuel

print(result)