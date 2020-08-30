import sys
sys.stdin = open("19238_스타트 택시.txt", "r")

from collections import deque
from queue import PriorityQueue

# 초기 데이터
N, M, fuel = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(N)]
taxi = list(map(lambda x: x-1, map(int, input().split())))
customers_data = [list(map(lambda x: x-1, map(int, input().split()))) for _ in range(M)]

# 내 데이터
is_arrived = [False] * M

def is_safe(map_data, start):
    L, x, y = len(map_data), start[0], start[1]
    return 0 <= x < L and 0 <= y < L and map_data[x][y] == 0

# 거리 측정하는 함수
def measure_distance(map_data, start, end):
    global fuel
    distance_map = [[0 for _ in range(N)] for _ in range(N)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    deq = deque()
    deq.append(start)

    while deq:
        temp = deq.popleft()
        x, y = temp[0], temp[1]

        if x == end[0] and y == end[1]: return distance_map[x][y]

        for i in range(4):
            test = [x + dx[i], y + dy[i]]
            test_x, test_y = test[0], test[1]

            if is_safe(map_data, test) and distance_map[test_x][test_y] == 0:
                distance_map[test_x][test_y] = distance_map[x][y] + 1
                deq.append(test)

    # 도착지에 도착 못하는 경우
    if distance_map[end[0]][end[1]] == 0: fuel = -1

    return -1


flag = True

# 최소거리 손님 탐색
for _ in range(M):
    customers = PriorityQueue()
    for i in range(M):
        if is_arrived[i] is False:
            depart, arrive = customers_data[i][:2], customers_data[i][2:]
            customers.put(
                [measure_distance(map_data, taxi, depart)] + depart + arrive + [i])

    customer = customers.get()
    customer_distance = customer[0]
    depart = customer[1:3]
    arrive = customer[3:5]
    customer_index = customer[5]

    # 손님 태울 수 있나?
    if customer_distance >= fuel:
        flag = False
        break
    else:
        fuel -= customer_distance
        taxi = depart

    # 도착지까지 갈 수 있나?
    destination_distance = measure_distance(map_data, taxi, arrive)
    if destination_distance > fuel:
        flag = False
        break
    else:
        fuel -= destination_distance
        is_arrived[customer_index] = True
        taxi = arrive
        fuel += 2 * destination_distance

if flag is True: print(fuel)
else: print(-1)